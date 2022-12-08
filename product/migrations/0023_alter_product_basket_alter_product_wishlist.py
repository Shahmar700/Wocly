# Generated by Django 4.1.1 on 2022-11-18 15:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0022_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='basket',
            field=models.ManyToManyField(blank=True, null=True, related_name='basket', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='wishlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
