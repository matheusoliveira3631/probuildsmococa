# Generated by Django 3.0 on 2020-06-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0009_auto_20200504_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='campeao',
            name='riot_key',
            field=models.CharField(blank=True, default=0, max_length=10),
        ),
    ]
