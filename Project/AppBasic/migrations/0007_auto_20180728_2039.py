# Generated by Django 2.0.7 on 2018-07-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBasic', '0006_auto_20180728_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamodel',
            name='Imagedata',
            field=models.ImageField(blank=True, upload_to='userpost_data'),
        ),
    ]