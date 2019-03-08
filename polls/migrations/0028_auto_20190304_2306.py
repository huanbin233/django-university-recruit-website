# Generated by Django 2.1.2 on 2019-03-04 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20190224_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_position',
            name='hot_val',
            field=models.IntegerField(default=0, verbose_name='热度值'),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='city',
            field=models.CharField(default='所有', max_length=80, verbose_name='就业城市'),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='edu_req',
            field=models.CharField(choices=[('1', '不限'), ('2', '专科'), ('3', '本科'), ('4', '硕士'), ('5', '博士')], default='5', max_length=2, verbose_name='学历要求'),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='exp_req',
            field=models.CharField(choices=[('1', '无'), ('2', '一年'), ('3', '两年'), ('4', '三年及以上')], default='1', max_length=2, verbose_name='工作经验'),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='job_desc',
            field=models.CharField(max_length=300, verbose_name='岗位描述'),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='name',
            field=models.CharField(default='', max_length=30, verbose_name='岗位'),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='publisher',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.HRProfile', verbose_name='发布者'),
        ),
    ]