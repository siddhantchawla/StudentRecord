# Generated by Django 2.1 on 2019-09-14 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20190914_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='course',
        ),
    ]
