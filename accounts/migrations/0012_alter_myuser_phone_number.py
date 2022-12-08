# Generated by Django 4.1.1 on 2022-09-12 10:24

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_myuser_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='phone number'),
        ),
    ]
