# Generated by Django 5.0 on 2024-05-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkinCareApp', '0002_routineskintype_skincareroutine_skincareproduct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skincareproduct',
            name='image_url',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='skincareproduct',
            name='product_url',
            field=models.URLField(max_length=500),
        ),
    ]