# Generated by Django 2.1.5 on 2019-02-18 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SoiHiso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_text', models.CharField(max_length=200)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoiHiso.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(default=0)),
                ('review_date', models.DateTimeField(verbose_name='date published')),
                ('review_text', models.CharField(max_length=300)),
                ('summary_text', models.CharField(max_length=500)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoiHiso.Restaurant')),
            ],
        ),
    ]