from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

#学生用户 的信息
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='StuProfile')
    name = models.CharField(max_length=50,verbose_name="姓名",blank=False,default='')
    gender = models.CharField(max_length=2, choices=(('1','男'),('2','女'),('3','未填写')),verbose_name="性别",blank=True,default='3')
    phone = models.CharField(max_length=200,verbose_name="联系方式",blank=True,default='')

    def __str__(self):
        return self.user.username

#人事专业HR 的信息
class HRProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='HRProfile')
    name = models.CharField(max_length=50,verbose_name="姓名",blank=False,default='')
    gender = models.CharField(max_length=2, choices=(('1','男'),('2','女'),('3','未填写')),verbose_name="性别",blank=True,default='3')
    phone = models.CharField(max_length=200,verbose_name="联系方式",blank=True,default='')

    company = models.CharField(max_length=100,verbose_name="公司",blank=False,default='')

    def __str__(self):
        return self.user.username

#教育经历
class Edu_experience(models.Model):
    edu_choice=(
        ('1','专科'),
        ('2','本科'),
        ('3','硕士'),
        ('4','博士'),
    )
    #时间段
    start_date         = models.DateField()
    end_date           = models.DateField()
    #学校
    gra_school         = models.CharField(max_length=150)
    #学历
    edu                = models.CharField(max_length=10,choices=edu_choice,default='1')
    #专业
    profession         = models.CharField(max_length=50,default='')
    owner              = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.profession

#项目经验
class Pro_experience(models.Model):
    #项目时间
    start_date         = models.DateField()
    end_date           = models.DateField()
    #项目角色
    job_role           = models.CharField(max_length=50)
    #项目名称
    job_name           = models.CharField(max_length=100)
    #项目描述
    job_desc           = models.CharField(max_length=200)

    owner              = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.job_name + ":" + self.job_role


#工作经历
class Job_experience(models.Model):
    #在职时间
    start_date         = models.DateField()
    end_date           = models.DateField()
    #公司名称
    company_name       = models.CharField(max_length=50,default='')
    #工作职位
    job_role           = models.CharField(max_length=50,default='')
    #工作描述
    job_desc           = models.CharField(max_length=200,default='')
    #所属行业
    industry           = models.CharField(max_length=50,default='')            

    owner              = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.company_name + "-" + self.job_role

#岗位信息
class Job_position(models.Model):
    edu_choice=(
        ('1','不限'),
        ('2','专科'),
        ('3','本科'),
        ('4','硕士'),
        ('5','博士'),
    )
    exp_choice=(
        ('1','无'),
        ('2','一年'),
        ('3','两年'),
        ('4','三年及以上'),
    )
    #岗位名字
    name               = models.CharField(max_length=30,verbose_name='岗位',default='')
    #工作描述
    job_desc           = models.CharField(max_length=300,verbose_name='岗位描述')
    #就业城市
    city               = models.CharField(max_length=80,default='所有',verbose_name='就业城市')
    #学历要求
    edu_req            = models.CharField(max_length=2,choices=edu_choice,default='5',verbose_name='学历要求')
    #工作经验要求
    exp_req            = models.CharField(max_length=2,choices=exp_choice,default='1',verbose_name='工作经验')
    #发布时间
    pub_date           = models.DateField(auto_now_add=True,verbose_name='发布时间')
    #发布者
    publisher          = models.ForeignKey(HRProfile,on_delete=models.CASCADE,default='',verbose_name='发布者')
    #薪资
    salary             = models.IntegerField(verbose_name='薪资',default=0)
    #热度值
    hot_val            = models.IntegerField(verbose_name='热度值',default=0)
    def __str__(self):
        return self.name


#投递信息
class SendResume(models.Model):
    stu                = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=False)
    sta                = models.ForeignKey(Job_position,on_delete=models.CASCADE,null=False)
    def __str__(self):
        return self.stu.name + " " + self.sta.name