# Generated by Django 4.0.2 on 2022-03-25 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0006_watchlist_avg_rating_watchlist_number_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewlist',
            name='platform',
        ),
    ]
