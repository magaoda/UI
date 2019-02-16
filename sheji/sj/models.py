from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
  phonetell=models.CharField(max_length=11)
  password=models.CharField(max_length=10)

class Issue(models.Model):
  c = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='发布')
  con=models.CharField(max_length=300)
  u_time = models.DateTimeField(auto_now=True)
  pl=models.TextField(max_length=100)
  zan=models.CharField(max_length=100)
  zhuan = models.CharField(max_length=100)
  img=models.CharField(max_length=100)

class ZL(models.Model):
  name=models.CharField(max_length=100)
  size=models.CharField(max_length=100)
  life=models.CharField(max_length=100)
  price=models.CharField(max_length=100)
  iq=models.CharField(max_length=100)
  breed=models.CharField(max_length=100)
