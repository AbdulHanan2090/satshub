# Generated by Django 3.2.8 on 2023-08-18 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='textsumerizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopic', models.CharField(blank=True, max_length=100, null=True)),
                ('topicname', models.CharField(blank=True, max_length=100, null=True)),
                ('lenthtopic', models.IntegerField(blank=True, null=True)),
                ('topic', models.CharField(blank=True, max_length=10000, null=True)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('time_field', models.TimeField(default=datetime.time(9, 8, 0, 931234))),
                ('summary', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]
