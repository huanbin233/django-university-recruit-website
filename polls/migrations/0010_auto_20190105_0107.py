# Generated by Django 2.1.2 on 2019-01-04 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20190105_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='resume',
        ),
        migrations.AddField(
            model_name='student',
            name='has_resume',
            field=models.IntegerField(default=0),
        ),
    ]