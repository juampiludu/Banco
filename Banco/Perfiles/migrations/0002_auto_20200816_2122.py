# Generated by Django 3.1 on 2020-08-17 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
