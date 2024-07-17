from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Todo(models.Model):
    status_choices = {
        ('c' , 'COMPLETED'),
        ('p' , 'PENDING'),

    }

    priority_choices = {
        ('1' , ' 1️⃣'),
        ('2' , ' 2️⃣'),
        ('3' , ' 3️⃣'),
        ('4' , ' 4️⃣'),
        ('5' , ' 5️⃣'),
        ('6' , ' 6️⃣'),
        ('7' , ' 7️⃣'),
        ('8' , ' 8️⃣'),
        ('9' , ' 9️⃣'),
        ('10' , '🔟'),

        


    }



    title = models.CharField(max_length=30)
    status =models.CharField(max_length=2 , choices = status_choices)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now=True)
    priority = models.CharField(max_length=2 , choices = priority_choices)
   


