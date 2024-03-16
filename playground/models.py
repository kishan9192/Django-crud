from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)

    ##### Read more about __str__ what does it do
    def __str__(self):
        return self.name