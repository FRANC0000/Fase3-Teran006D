# Generated by Django 3.1.2 on 2020-10-26 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermercado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
