from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sername = models.CharField(max_length=100)
    
    

    def __str__(self):
        return self.name