# Generated by Django 2.1.2 on 2019-03-10 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0037_auto_20190310_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrprofile',
            name='identify',
            field=models.CharField(choices=[('1', '已认证'), ('2', '未认证')], default='2', max_length=2, verbose_name='认证'),
        ),
    ]
