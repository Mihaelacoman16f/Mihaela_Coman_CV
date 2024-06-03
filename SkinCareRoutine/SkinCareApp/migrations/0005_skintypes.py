# Generated by Django 5.0 on 2024-05-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkinCareApp', '0004_skincareproduct_description_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkinTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('advantages', models.TextField()),
                ('disadvantages', models.TextField()),
            ],
        ),
    ]