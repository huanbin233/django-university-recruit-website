# Generated by Django 2.1.2 on 2019-03-21 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0040_auto_20190320_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify_h',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.SendResume')),
            ],
        ),
    ]
