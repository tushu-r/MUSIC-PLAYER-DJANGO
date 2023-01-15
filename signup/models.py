from django.db import models


# Create your models here.
class USER(models.Model):
    no = models.IntegerField(blank = True )
    username = models.CharField( max_length = 255 )
    directory = models.CharField( max_length = 255 ,null = False , blank = False)
    email = models.EmailField( max_length = 255 , blank = False , null = False)
   
  

    def __str__(self):
        return self.username
    


  