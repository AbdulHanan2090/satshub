# Generated by Django 3.2.8 on 2023-11-27 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20231127_1342'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fileadmin',
        ),
        migrations.DeleteModel(
            name='Filesumerizer',
        ),
        migrations.DeleteModel(
            name='textsumerizer',
        ),
    ]
