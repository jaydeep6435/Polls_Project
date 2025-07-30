from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib import admin


# Create your models here.
# in question class - question and publication datetime
# in choice class - choice txt and votes 
class Questions(models.Model):        # models.model it means it inherite the model class 
    ques_txt=models.CharField(max_length=200)        # charfield and datetimefield  denotes datatypes of question and time  
    publ_time=models.DateTimeField(default=timezone.now())  # now() represent  current timing of raising a qustion by user 
    #def __str__(self):
        #return self.ques_txt
        
    @admin.display(
        boolean=True,
        ordering='publ_time',
        description='published recently?',
    )
    
    def was_question_recently_published(self):
        return self.publ_time>= timezone.now()-datetime.timedelta(1)
    
    
    
    
class Choice(models.Model):
    choice_txt=models.CharField(max_length=200)
    votes=models.IntegerField(default=1)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)      # this line coonets thse two classes , forigenkey inherit the Questions  
   # (on_delete=models.cascade) it means if questions is deleted then there votes for question is pointingless thats why we used  this  & CASCADE its is proceed one by one   
    def __str__(self):
        return self.choice_txt
    
