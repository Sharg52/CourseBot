# Generated by Django 3.0.5 on 2020-05-04 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20200504_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
    ]
