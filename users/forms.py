from urllib import request
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
from product.models import Product, Invoice
from accounts.options import USERTYPE
from ckeditor.widgets import CKEditorWidget

from users.models import Vendor


# get custom user
User = get_user_model()

class BuyerDetailForm(forms.ModelForm):
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

    birthday=forms.CharField(required=False,widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type':'date'
        
    	}))

    phone_number = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'type':'number'
        }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control'
    }))

    usertype = forms.CharField(widget=forms.Select(choices=USERTYPE,attrs={
        'class':'form-control'
    }))
    
    
    # phone_number=
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
        fields = ('first_name','birthday','last_name','email','phone_number','image','usertype')







class SellerDetailForm(forms.ModelForm):
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

    birthday=forms.CharField(required=False,widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type':'date'
        
    	}))

    phone_number = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'type':'number'
        }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control'
    }))

    company_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

    usertype = forms.CharField(widget=forms.Select(choices=USERTYPE,attrs={
        'class':'form-control'
    }))
    
    # phone_number=
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
        fields = ('first_name','birthday','last_name','email','phone_number','image','usertype','company_name')



class AdminDetailForm(forms.ModelForm):
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

    birthday=forms.CharField(required=False,widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type':'date'
        
    	}))

    phone_number = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'type':'number'
        }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control'
    }))

    usertype = forms.CharField(widget=forms.Select(choices=USERTYPE,attrs={
        'class':'form-control'
    }))
    
    
    # phone_number=
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
        fields = ('first_name','birthday','last_name','email','phone_number','image','usertype')


class AddProductForm(forms.ModelForm):
    
    # name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
    # 	'placeholder':'Product Name',
    #     'autofocus': '',
    #     'class' : 'form-control'
    # 	}))
    # description=forms.CharField(max_length=1200,widget=CKEditorWidget())

    # price=forms.IntegerField(widget=forms.NumberInput(attrs={
    #     'type':'number'
        
    # 	}))

    # # category = forms.ChoiceField(widget=forms.Select(attrs={
    # #     'type':'number'
    # #     }))

    # image = forms.ImageField(widget=forms.FileInput(attrs={
    #     'class':'form-control'
    # }))

    # discount=forms.IntegerField(widget=forms.NumberInput(attrs={
    #     'type':'number'
        
    # 	}))

    
    
    


    class Meta:
        model = Product
        exclude = ('seller','sold','draft','slug','basket','wishlist','tempamount')
        fields = ('__all__')



class VendorForm(forms.ModelForm):
    image=forms.FileField(max_length=100,widget=forms.FileInput(attrs={
    	'id':'uploadbanner',
        'type':'file',
        'style':'display: none;',
        
    	}))



    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    	'placeholder':'Store Name',
        'autofocus': '',
        
    	}))

    # description=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    # 	'placeholder':'Store Name',
    #     'autofocus': '',
        
    # 	}))

    email=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    	'placeholder':'Store Email',
        
        
    	}))

    street_1=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    	'placeholder':'Street adress',
        
        
    	}))

    street_2=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    	'placeholder':'Apartment, suite, unit etc. (optional)',
        'requiered':'false'
        
        
    	}))

    city=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    	'placeholder':'Town / City',
        
        
    	}))

    zip=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    	'placeholder':'Postcode / Zip',
        
        
    	}))

    phone_number=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
    	'placeholder':'+994...',
        
        
    	}))



    class Meta:
        model = Vendor
        exclude = ('seller',)
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class ChangeStatusForm(forms.ModelForm):
    
    # name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
    # 	'placeholder':'Product Name',
    #     'autofocus': '',
    #     'class' : 'form-control'
    # 	}))
    # description=forms.CharField(max_length=1200,widget=CKEditorWidget())

    # price=forms.IntegerField(widget=forms.NumberInput(attrs={
    #     'type':'number'
        
    # 	}))

    # # category = forms.ChoiceField(widget=forms.Select(attrs={
    # #     'type':'number'
    # #     }))

    # image = forms.ImageField(widget=forms.FileInput(attrs={
    #     'class':'form-control'
    # }))

    # discount=forms.IntegerField(widget=forms.NumberInput(attrs={
    #     'type':'number'
        
    # 	}))

    class Meta:
        model = Invoice
        
        fields = ('status',)

