from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField, CaptchaTextInput
from django.forms.widgets import SelectDateWidget
from .models import *

class UserForm(forms.Form):
	user_input= forms.CharField(max_length=200)

class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Логин'}))
	email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
	password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
	captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class':'form-control', 'placeholder': 'Введите текст с картинки', 'style': 'padding: 6px;'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Логин'}))
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Пароль'}))
	captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class':'form-control', 'placeholder': 'Введите текст с картинки', 'style': 'padding: 6px;'}))

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_pic', 'bio', 'location', 'birth_date']

class UpdateUserForm(forms.ModelForm):
	username = forms.CharField(max_length=100,
							   required=True,
							   widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=20,
							   required=False,
							   widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=20,
							   required=False,
							   widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(required=True,
							 widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
	bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
	location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	birth_date = forms.DateField(widget=SelectDateWidget(years=range(1950, 2020), empty_label=("Choose Year", "Choose Month", "Choose Day"),),)
	class Meta:
		model = Profile
		fields = ['bio', 'location', 'birth_date']

class User_dialoguesForm(forms.ModelForm):
	name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
	setting = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
	character_name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
	character_background = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

	class Meta:
		model = User_dialogues
		fields = ['name', 'setting', 'character_name', 'character_background']

		
class User_inputForm(forms.ModelForm):
	user_input = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Начните писать', 'id':'textarea_ui', 'rows': 3}))

	class Meta:
		model = Dialogue
		fields = ['user_input']

class input_for_AI_img(forms.Form):
	user_input_img = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Начните писать', 'id':'user_input_img', 'rows': 3}))

	class Meta:
		fields = ['user_input_img']

class Params(forms.Form):
	seed = forms.CharField(max_length=200)
	lora_alpha = forms.CharField(max_length=200)
	cfg_scale = forms.CharField(max_length=200)
	tmp = forms.CharField(max_length=200)
	mnt = forms.CharField(max_length=200)

