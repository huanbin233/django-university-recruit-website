# Generated by Django 2.1.2 on 2019-05-05 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0058_auto_20190505_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendresume',
            name='check',
        ),
    ]
