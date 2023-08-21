# Generated by Django 4.0.1 on 2022-11-16 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0005_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
