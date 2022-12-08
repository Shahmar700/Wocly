from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
from django.conf import settings
from django.core import validators
from django.utils.translation import gettext_lazy as _
from product.helper import seo
from phonenumber_field.modelfields import PhoneNumberField
from accounts.options import USERTYPE
from phone_field import PhoneField
USER_MODEL = settings.AUTH_USER_MODEL



class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), null=True, max_length=100, unique=False)
    first_name = models.CharField(_('first name'), max_length=255, blank=True, )
    company_name = models.CharField(_('company name'), max_length=50, blank=True)
    phone_number = PhoneField(_("phone number"), blank=True, null=True)
    birthday = models.DateField(_("birth date"), blank=True, null=True)
    usertype = models.IntegerField(verbose_name="Cins",choices=USERTYPE,null=True,blank=True,default=1)

    image = models.ImageField(_("image"),null=True,blank=True,upload_to="user_pp")
    
    last_name = models.CharField(_('last name'), max_length=255, blank=True)
    image=models.ImageField(_('Add Photo'),null=True)

    email = models.EmailField(_('email address'), unique=True, max_length=255, blank=False)

    slug = models.SlugField(unique=True, editable=False, null=True)

    is_buyer = models.BooleanField(_('user buyer'), default=False)
    
    is_seller = models.BooleanField(_('user seller'), default=False)

    is_pro = models.BooleanField(_('pro seller'), default=False)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()




    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        managed = True

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        super(MyUser, self).save(*args, **kwargs)
        self.slug = "{}.{}".format(seo(self.first_name + "-" + self.last_name), self.id)
        super(MyUser, self).save(*args, **kwargs)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()

    def get_avatar(self):
        if self.image:
            return self.image.url
        elif self.usertype == 1:
            return "/static/img/man_avatar.png"
        elif self.usertype == 2:
            return "/static/img/woman_avatar.jpg"
        