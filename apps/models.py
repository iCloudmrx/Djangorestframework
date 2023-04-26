from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=250)
    subtitle=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    isbt = models.CharField(max_length=13)
    price=models.DecimalField(max_digits=20,decimal_places=2)

    def __str__(self):
        return self.title
