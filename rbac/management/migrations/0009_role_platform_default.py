# Generated by Django 2.2.4 on 2019-11-22 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_group_platform_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='platform_default',
            field=models.BooleanField(default=False),
        ),
    ]
