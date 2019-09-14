# Generated by Django 2.2.5 on 2019-09-10 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0016_auto_20190909_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='author',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='likes',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/(Photo.id)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photosession',
            name='img',
            field=models.ImageField(upload_to='media/Photosession'),
        ),
    ]
