# Generated by Django 3.0.7 on 2020-07-31 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banking',
            name='cvu',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
