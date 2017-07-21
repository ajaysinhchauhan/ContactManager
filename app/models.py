from django.db import models
import datetime

class Contact(models.Model):
   FirstName = models.CharField( max_length=50, null=True)
   LastName = models.CharField( max_length=50)
   Email =  models.EmailField(max_length=50)
   Mobile = models.DecimalField(max_digits=12, decimal_places=0)