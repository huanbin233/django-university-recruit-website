# Generated by Django 2.1.2 on 2019-03-10 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0035_auto_20190310_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='img_id',
            field=models.IntegerField(default=0, verbose_name='图片ID'),
        ),
    ]
