from django.db import models


# Create your models here.
class Massage(models.Model):
    name = models.CharField(max_length=120, verbose_name= "Имя")
    email = models.EmailField(max_length=240,verbose_name="email")
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



