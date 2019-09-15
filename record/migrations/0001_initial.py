# Generated by Django 2.1 on 2019-09-14 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regNum', models.CharField(max_length=10)),
                ('status', models.IntegerField(max_length=2)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
