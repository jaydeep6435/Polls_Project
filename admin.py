from django.contrib import admin

# Register your models here.
from .models import Questions,Choice

class choiceinline(admin.TabularInline):
    model=Choice
    extra =1
    
    



class Pollsadmins(admin.ModelAdmin):
    fieldsets=[
               #{None,{'field['ques_txt']}},
               #{'date information',{'field':['pub_date']}}
               ]
    inlines=[choiceinline]
    list_display=('ques_txt','publ_time')
    list_filter=['publ_time']
    search_fields=['ques_txt']
    
    

admin.site.register(Questions,Pollsadmins)
#admin.site.register(Choice)