# Generated by Django 2.2.5 on 2019-09-06 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0004_auto_20190906_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestSites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='best_sites_img')),
                ('content', models.TextField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
    ]
