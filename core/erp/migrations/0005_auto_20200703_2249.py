# Generated by Django 3.0.7 on 2020-07-04 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20200703_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cate',
            new_name='cat',
        ),
    ]
