# Generated by Django 2.2.5 on 2019-09-09 08:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0014_auto_20190908_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='photosession',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/Photosession'),
            preserve_default=False,
        ),
    ]
