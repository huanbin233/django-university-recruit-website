# Generated by Django 2.1.2 on 2019-01-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20190105_0107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company_name',
        ),
        migrations.AddField(
            model_name='company',
            name='passwd',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='company',
            name='username',
            field=models.CharField(default='user', max_length=100),
        ),
    ]