from django.db import models

# Create your models here.
class user_registration(models.Model):
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    Username = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    def __str__(self):
        return self.Fname



class reg(models.Model):
  Drname= models.CharField(max_length=20)
  Department= models.CharField(max_length=20)
  Pnum=models.IntegerField()
  def __str__(self):
    return self.Drname

class feedback(models.Model):
   Name= models.CharField(max_length=20)
   Email= models.CharField(max_length=20)
   Message= models.CharField(max_length=20)
   def __str__(self):
    return self.Email



