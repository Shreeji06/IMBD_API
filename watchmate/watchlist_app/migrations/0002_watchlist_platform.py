# Generated by Django 4.0.2 on 2022-03-04 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='WatchList', to='watchlist_app.streamplatform'),
            preserve_default=False,
        ),
    ]
