# Generated by Django 2.2 on 2020-01-31 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewpoint', '0010_auto_20200131_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packageimage',
            options={'verbose_name': '套餐照片', 'verbose_name_plural': '套餐照片'},
        ),
        migrations.AlterField(
            model_name='packageimage',
            name='intr',
            field=models.CharField(default='', max_length=100, verbose_name='描述'),
        ),
        migrations.CreateModel(
            name='ViewImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='images/%Y/%m', verbose_name='景点照片')),
                ('intr', models.CharField(default='', max_length=100, verbose_name='描述')),
                ('view_img_list', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='viewpoint.Viewpoint')),
            ],
            options={
                'verbose_name_plural': '景点照片',
                'verbose_name': '景点照片',
            },
        ),
    ]