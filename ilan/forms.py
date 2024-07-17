from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, EmailField, SubmitField, SelectField
from wtforms.validators import DataRequired, length
from flask_wtf.file import FileField, FileRequired


class SignUpForm(FlaskForm):
    email = EmailField('E-posta', validators=[DataRequired()]) 
    username = StringField('Kullanıcı Adı', validators=[DataRequired(), length(min=2)]) 
    password1 = PasswordField('Parolanızı Girin', validators=[DataRequired(), length(min=6)]) 
    password2 = PasswordField('Parolanızı Onaylayın', validators=[DataRequired(), length(min=6)]) 
    submit = SubmitField('Üye Ol')


class LoginForm(FlaskForm):
    email = EmailField('E-posta', validators=[DataRequired()])  
    password = PasswordField('Parolanızı Girin', validators=[DataRequired()])  
    submit = SubmitField('Giriş Yap') 


class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Mevcut Parola', validators=[DataRequired(), length(min=6)]) 
    new_password = PasswordField('Yeni Parola', validators=[DataRequired(), length(min=6)]) 
    confirm_new_password = PasswordField('Yeni Parolanızı Onaylayın', validators=[DataRequired(), length(min=6)])  
    change_password = SubmitField('Parolayı Değiştir') 


class ShopItemsForm(FlaskForm):
    product_name = StringField('Başlık', validators=[DataRequired()]) 
    current_price = FloatField('Güncel Fiyat', validators=[DataRequired()]) 
    product_picture = FileField('Resim', validators=[FileRequired()]) 
    add_product = SubmitField('Ekle')
    update_product = SubmitField('Güncelle')

