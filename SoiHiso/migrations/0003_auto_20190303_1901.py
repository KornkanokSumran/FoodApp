# Generated by Django 2.1.5 on 2019-03-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoiHiso', '0002_menu_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='office_hours',
            field=models.CharField(default='', max_length=200),
        ),
    ]
