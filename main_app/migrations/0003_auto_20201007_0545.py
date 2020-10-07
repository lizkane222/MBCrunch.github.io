# Generated by Django 3.1.2 on 2020-10-07 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201007_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection_market',
            name='location',
            field=models.TextField(default='Address:', max_length=250),
        ),
        migrations.AddField(
            model_name='collection_market',
            name='market_description',
            field=models.TextField(default='Community Centered Market', max_length=300),
        ),
    ]
