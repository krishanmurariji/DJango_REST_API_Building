import uuid
from django.db import models

# Create your models here.
# class employee (models.Model):
#     fname = models.CharField(max_length=200)
#     lname = models.CharField(max_length=200)
#     contact = models.IntegerField()
class Group (models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    contact = models.IntegerField()
class Car(models.Model):
    cname = models.CharField(max_length=200)
    cspeed = models.IntegerField()
class Product(models.Model):
    pid = models.CharField(max_length=200)
    pname = models.CharField(max_length=200)
    pprice = models.CharField(max_length=200)
class Storage(models.Model):
    sid=models.CharField(max_length=200)
    sname=models.CharField(max_length=200)
    sprice=models.IntegerField()
class Name(models.Model):
    fname = models.CharField( max_length=50)
    lname = models.CharField( max_length=50)

class BaseMOdel(models.Model):
    uid = models.UUIDField(primary_key= True, editable=False, default = uuid.uuid4()) 
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now_add = True)
    
    class Meta:
        abstract = True

class Todo(BaseMOdel):
    title = models.CharField(max_length = 100)
    discription = models.TextField()
    id_done = models.BooleanField(default = False)

class Contacts(models.Model):
    cid = models.IntegerField()
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    add = models.CharField(max_length = 100)
    dis = models.TextField()