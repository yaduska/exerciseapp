# Generated by Django 4.2.7 on 2023-12-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietplan',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
