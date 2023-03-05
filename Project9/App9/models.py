from django.db import models

# Create your models here.
class Data(models.Model):
   sepal_length = models.FloatField(max_length=5)
   sepal_width = models.FloatField(max_length=5)
   petal_length = models.FloatField(max_length=5)
   petal_width = models.FloatField(max_length=5)