# Generated by Django 2.0.7 on 2018-07-29 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBasic', '0008_auto_20180729_0834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datamodel',
            old_name='Describe',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='datamodel',
            old_name='Imagedata',
            new_name='Select_Your_Image',
        ),
    ]
