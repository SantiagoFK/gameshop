# Games App models

from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=250)
    developer = models.CharField(max_length=250)
    #publisher = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release = models.DateField()
    #genre = models.CharField()
    cover = models.ImageField(upload_to='covers/', blank=True)
    
    def __str__(self):
        return self.title
    
'''
Notes: 
1) genre should be a list of tags, but also a one to many field. 
Ex: RPG, Action, Fantasy

2) some fields are commented here, for the sake of simplicity on initial tests.

* Seria buena idea abstraer la cantidad de digitos necesarios para el campo price.

'''