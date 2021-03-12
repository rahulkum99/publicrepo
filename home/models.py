from django.db import models


# Create your models here.
class Categorie(models.Model):
    tille = models.CharField(max_length=30)

    def __str__(self):
        return self.tille
    
class Blogpost(models.Model):
    slno = models.AutoField(primary_key = True)
    title = models.CharField(max_length= 100)
    overview = models.TextField()
    time_upload = models.DateTimeField(blank=True)
    author = models.CharField(max_length=25)
    slug = models.CharField(max_length=130,default="")
    thumbnail = models.ImageField(upload_to = 'thumbnails')
    publish = models.BooleanField()
    categories = models.ManyToManyField(Categorie)

    class Meta:
        ordering = ['-time_upload',]
        
    def __str__(self):
        return self.title + '  '+ self.author

class Contect(models.Model):
    slno = models.AutoField(primary_key = True)
    fname = models.CharField(max_length=25)
    Lname = models.CharField(max_length=25)
    email = models.EmailField()
    mob = models.IntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.fname + '  '+ self.email