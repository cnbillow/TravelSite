# Generated by Django 2.2 on 2020-01-31 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewpoint', '0003_auto_20200131_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': '照片', 'verbose_name_plural': '照片'},
        ),
        migrations.RemoveField(
            model_name='travelpackage',
            name='pics',
        ),
    ]
