# Generated by Django 3.1.3 on 2020-11-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinksMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(max_length=128, verbose_name='категория')),
                ('name', models.CharField(max_length=128, verbose_name='название')),
            ],
        ),
        migrations.CreateModel(
            name='SameProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название')),
                ('image_src', models.ImageField(blank=True, upload_to='products_images', verbose_name='картинка')),
                ('desc', models.CharField(blank=True, max_length=120, verbose_name='краткое описание')),
                ('alt', models.TextField(blank=True, verbose_name='картинка')),
            ],
        ),
    ]
