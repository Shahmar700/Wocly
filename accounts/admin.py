from django.contrib import admin
# from accounts.forms import MyUserChangeForm, MyUserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import *




User = get_user_model()
@admin.register(User)
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name','image','company_name','birthday','phone_number','usertype')}),
        (_('Permissions'), {'fields': ('is_active','is_buyer','is_seller','is_superuser',
                                       'groups', 'user_permissions','is_pro')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("first_name", "last_name", 'email', 'password1', 'password2'),
        }),
    )
    # # The forms to add and change user instances
    # form = MyUserChangeForm
    # add_form = MyUserCreationForm
    list_display = ('first_name','last_name','email','is_superuser','is_active')
    list_display_links=('first_name','last_name','email')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups','is_buyer','is_seller','is_pro')
    # search_fields = ('first_name', 'last_name', 'email')
    # ordering = ('-date_joined',)
    # filter_horizontal = ('groups', 'user_permissions',)

