# Generated by Django 3.0.5 on 2020-04-30 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_auto_20200430_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='referral',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='кто пригласил'),
        ),
    ]
