# Generated by Django 2.2.4 on 2020-09-28 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("management", "0022_auto_20201022_1337")]

    operations = [migrations.RemoveField(model_name="access", name="permission")]
