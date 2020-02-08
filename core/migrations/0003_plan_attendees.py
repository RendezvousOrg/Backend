# Generated by Django 3.0.2 on 2020-02-08 16:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200122_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='attendees',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]