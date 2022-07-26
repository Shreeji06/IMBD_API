# Generated by Django 4.0.2 on 2022-03-08 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watchlist_app', '0003_reviewlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewlist',
            old_name='descrptions',
            new_name='descriptions',
        ),
        migrations.AddField(
            model_name='reviewlist',
            name='review_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]