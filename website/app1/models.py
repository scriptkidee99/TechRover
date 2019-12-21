from django.db import models

# Create your models here.

class Blog(models.Model):
    show_img = models.CharField(max_length=500,default='/media/imgicon.png')
    full_img = models.CharField(max_length=500,default='/media/imgicon.png')
    title = models.CharField(max_length=300,default='')
    content = models.TextField(default='')
    key = models.CharField(default = '-1',max_length=5)

    
class Users(models.Model):
	fname = models.CharField(max_length=30,default = '')
	lname = models.CharField(max_length=30,default = '')
	email = models.CharField(max_length=50,default = '')
	passwd = models.CharField(max_length=30,default = '')
	fblogs = models.CharField(max_length=1000,default='')
	verified = models.CharField(max_length=1,default='N')

	def __str__(self):
		return str(str(self.fname) + ' ' + str(self.lname))
    