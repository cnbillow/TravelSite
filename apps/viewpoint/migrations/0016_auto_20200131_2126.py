# Generated by Django 2.2 on 2020-01-31 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewpoint', '0015_auto_20200131_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packageimage',
            name='addtime',
        ),
        migrations.RemoveField(
            model_name='viewimage',
            name='addtime',
        ),
        migrations.AlterField(
            model_name='viewimage',
            name='view_img_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='viewpoint.Viewpoint'),
        ),
    ]
