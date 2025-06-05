from django.db import models

# Create your models here.
class Meg_tbl(models.Model):
    fnm=models.CharField(max_length=25)
    mob=models.IntegerField()
    eml=models.EmailField()
    psw=models.CharField(max_length=16)
class ME_tbl(models.Model):
    mnm = models.CharField(max_length=25)
    im= models.FileField(upload_to='pic')
    prc=models.IntegerField()
    des=models.TextField()
