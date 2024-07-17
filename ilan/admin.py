from flask import Blueprint, render_template, flash, send_from_directory, redirect,url_for
from flask_login import login_required, current_user
from .forms import ShopItemsForm
from werkzeug.utils import secure_filename
from .models import Product, Customer
from . import db
import os
admin = Blueprint('admin', __name__)

@admin.route('/media/<path:filename>')
def get_image(filename):
    return send_from_directory('../media',filename)


# @admin.route('/ilan-ekle', methods=['GET', 'POST'])
# @login_required
# def add_shop_items():
#         form = ShopItemsForm()
#         if form.validate_on_submit():
#             product_name = form.product_name.data
#             current_price = form.current_price.data

#             file = form.product_picture.data
#             file_name = secure_filename(file.filename)
#             file_path = f'./media/{file_name}'

#             file.save(file_path)
#             new_shop_item = Product()
#             new_shop_item.product_name = product_name
#             new_shop_item.current_price = current_price
#             new_shop_item.product_picture = file_path

#             try:
#                 db.session.add(new_shop_item)
#                 db.session.commit()
#                 flash(f'{product_name} başarıyla eklendi', 'success')
#                 return redirect(url_for('admin.add_shop_items'))
#             except Exception as e:
#                 print(e)
#                 flash('ilan eklenemedi', 'danger')
#                 return render_template('ilan_ekle.html', form=form)

#         return render_template('ilan_ekle.html', form=form)




@admin.route('/ilan-ekle', methods=['GET', 'POST'])
@login_required
def add_shop_items():
        form = ShopItemsForm()
        if form.validate_on_submit():
            product_name = form.product_name.data
            current_price = form.current_price.data
            

            file = form.product_picture.data
            file_name = secure_filename(file.filename)
            media_dir = './media'
            if not os.path.exists(media_dir):
                os.makedirs(media_dir)
            file_path = os.path.join(media_dir, file_name)

            try:
                file.save(file_path)
                new_shop_item = Product()
                new_shop_item.product_name = product_name
                new_shop_item.current_price = current_price
                new_shop_item.product_picture = file_path

                db.session.add(new_shop_item)
                db.session.commit()
                flash(f'{product_name} başarıyla eklendi', 'success')
                return redirect(url_for('admin.add_shop_items'))
            except Exception as e:
                print(e)
                flash('İlan eklenemedi', 'danger')
                return render_template('ilan_ekle.html', form=form)

        return render_template('ilan_ekle.html', form=form)



@admin.route('/shop-items', methods=['GET', 'POST'])
@login_required
def shop_items():
    if current_user.id == 1:
        items = Product.query.order_by(Product.date_added).all()
        return render_template('shop_items.html', items=items)
    return render_template('404.html') 


@admin.route('/update-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def update_item(item_id):
    if current_user.id == 1:
        form = ShopItemsForm()

        item_to_update = Product.query.get(item_id)

        form.product_name.render_kw = {'placeholder': item_to_update.product_name}
        form.current_price.render_kw = {'placeholder': item_to_update.current_price}

        if form.validate_on_submit():
            product_name = form.product_name.data
            current_price = form.current_price.data

            file = form.product_picture.data

            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'

            file.save(file_path)
            try:
                Product.query.filter_by(id=item_id).update(dict(product_name=product_name,
                                                                current_price=current_price,
                                                                product_picture=file_path))

                db.session.commit()
                flash(f'{product_name} başarıyla güncellendi')
                return redirect('/shop-items')
            except Exception as e:
                flash('ilan güncellendi')


        return render_template('update_item.html', form=form)
    return render_template('404.html')

@admin.route('/delete-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def delete_item(item_id):
    if current_user.id == 1:
        try:
            item_to_delete = Product.query.get(item_id)
            db.session.delete(item_to_delete)
            db.session.commit()
            flash('ilan silindi')
            return redirect('/shop-items')
        except Exception as e:
            flash('ilan silinemedi!')
        return redirect('/shop-items')

    return render_template('404.html')





@admin.route('/customers')
@login_required
def display_customers():
    if current_user.id == 1:
        customers = Customer.query.all()
        return render_template('customers.html', customers=customers)
    return render_template('404.html')


@admin.route('/admin-page')
@login_required
def admin_page():
    if current_user.id == 1:
        return render_template('admin.html')
    return render_template('404.html')