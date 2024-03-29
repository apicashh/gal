# Generated by Django 2.2.5 on 2019-09-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0006_auto_20190906_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='GallerySMC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField()),
                ('thumb', models.URLField()),
                ('direct_url', models.URLField()),
                ('site_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Gallery',
            new_name='GalleryIsland',
        ),
        migrations.AlterField(
            model_name='bestsite',
            name='image',
            field=models.ImageField(upload_to='media/best_sites_img'),
        ),
    ]
