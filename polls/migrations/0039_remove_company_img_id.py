# Generated by Django 2.1.2 on 2019-03-10 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0038_hrprofile_identify'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='img_id',
        ),
    ]
