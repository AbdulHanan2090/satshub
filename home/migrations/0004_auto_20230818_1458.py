# Generated by Django 3.2.8 on 2023-08-18 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_textsumerizer_time_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filesumerizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopic', models.CharField(blank=True, max_length=100, null=True)),
                ('topicname', models.CharField(blank=True, max_length=100, null=True)),
                ('lenthtopic', models.IntegerField(blank=True, null=True)),
                ('topic', models.CharField(blank=True, max_length=10000, null=True)),
                ('File', models.FileField(blank=True, null=True, upload_to='Media')),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('userid', models.IntegerField(blank=True, null=True)),
                ('time_field', models.TimeField(default=datetime.time(9, 58, 1, 568208))),
                ('summary', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='textsumerizer',
            name='time_field',
            field=models.TimeField(default=datetime.time(9, 58, 1, 568208)),
        ),
    ]
