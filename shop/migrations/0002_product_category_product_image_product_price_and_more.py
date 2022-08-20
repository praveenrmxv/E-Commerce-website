# Generated by Django 4.0.1 on 2022-01-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='image/'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='obc', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default=''),
        ),
    ]
