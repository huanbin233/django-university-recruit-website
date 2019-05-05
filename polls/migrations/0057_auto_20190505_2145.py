# Generated by Django 2.1.2 on 2019-05-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0056_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notify_h',
            name='delivery',
        ),
        migrations.AddField(
            model_name='sendresume',
            name='check',
            field=models.CharField(choices=[('1', '已查看'), ('0', '未查看')], default='1', max_length=2, verbose_name='查看状态'),
        ),
        migrations.DeleteModel(
            name='Notify_h',
        ),
    ]
