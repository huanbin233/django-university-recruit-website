from django.contrib import admin

from .models import Edu_experience,Pro_experience,Job_experience,Job_position,UserProfile,HRProfile,SendResume,Company,Notify_h
admin.site.register(Edu_experience)
admin.site.register(UserProfile)
admin.site.register(Job_experience)
admin.site.register(Pro_experience)
admin.site.register(Job_position)
admin.site.register(HRProfile)
admin.site.register(SendResume)
admin.site.register(Company)
admin.site.register(Notify_h)

# Register your models here.