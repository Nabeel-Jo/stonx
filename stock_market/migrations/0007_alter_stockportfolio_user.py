# Generated by Django 3.2.7 on 2021-11-13 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_market', '0006_auto_20211113_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockportfolio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
