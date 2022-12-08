from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from accounts.models import *
from PIL import Image
from users.models import *

# get custom user
User = get_user_model()

class BuyerRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'class':'form-control ',
        'placeholder':'Email',
        }
    ))
    first_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
    	'class':'form-control',
    	'placeholder':'Ad',
        'autofocus': '',
    	}))
    last_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Soyad'
        }))
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Şifrə'
        }
    ))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Şifrəni doğrula'
        }
    ))


    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = MyUser.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Bu email artıq mövcuddur.Yenisini yoxlayın!')
    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            match = MyUser.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Bu istifadəçi adı artıq mövcuddur.Yenisini yoxlayın!')

class SellerRegisterForm(UserCreationForm):

    company_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
    	'class':'form-control',
    	'placeholder':'Ad',
    	}))
    
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'class':'form-control ',
        'placeholder':'Email',
        }
    ))
    first_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
    	'class':'form-control',
    	'placeholder':'Ad',
    	}))
    last_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Soyad'
        }))
    # password1=forms.CharField(max_length=100,widget=forms.PasswordInput(
    #     attrs={
    #     'class':'form-control',
    #     'placeholder':'Şifrə'
    #     }
    # ))
    # password2=forms.CharField(max_length=100,widget=forms.PasswordInput(
    #     attrs={
    #     'class':'form-control',
    #     'placeholder':'Şifrəni doğrula'
    #     }
    # ))


    class Meta:
        model = User
        fields = ('company_name','first_name','last_name','email')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = MyUser.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Bu email artıq mövcuddur.Yenisini yoxlayın!')
    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            match = MyUser.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Bu istifadəçi adı artıq mövcuddur.Yenisini yoxlayın!')

class LoginForm(forms.Form):
	email= forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
        }
    ))
	password=forms.CharField(max_length=100,widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Şifrə'
        }
    ))

	def clean(self):
		email=self.cleaned_data.get('email')
		password=self.cleaned_data.get('password')
		if email and password:
			user=authenticate(email=email,password=password)
			if not user:
				raise forms.ValidationError('Email or Password is incorrect')
		return super(LoginForm, self).clean()


# class VendorRegisterForm(forms.ModelForm):
#     class Meta:
#         model = Vendor
#         fields = "__all__"