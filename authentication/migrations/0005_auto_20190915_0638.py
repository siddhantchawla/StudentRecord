# Generated by Django 2.1 on 2019-09-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20190915_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='contact',
            field=models.CharField(max_length=20),
        ),
    ]
