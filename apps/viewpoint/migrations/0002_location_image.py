# Generated by Django 2.2 on 2020-01-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewpoint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.ImageField(default='', upload_to='images/%Y/%m', verbose_name='照片'),
        ),
    ]
