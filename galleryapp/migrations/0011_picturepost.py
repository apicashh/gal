# Generated by Django 2.2.5 on 2019-09-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0010_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicturePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
    ]
