from django.contrib import admin

# Register your models here.
from app.models import *
from app.forms import *


class dispaly(admin.ModelAdmin):
    list_display=['s_id','s_name','s_mail']
    

admin.site.register(Student,dispaly)