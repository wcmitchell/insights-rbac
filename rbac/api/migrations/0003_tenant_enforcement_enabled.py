# Generated by Django 2.2.4 on 2019-10-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='enforcement_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
