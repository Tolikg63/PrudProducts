from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Dishes(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    calories = models.FloatField()
    weight = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title