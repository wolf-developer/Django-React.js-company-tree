# Generated by Django 3.1.6 on 2021-03-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20210221_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aresponse',
            name='uuid',
            field=models.CharField(default='', max_length=50, verbose_name='Uuid'),
        ),
    ]
