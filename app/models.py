from django.db import models


class Questions(models.Model):
    question = models.CharField(max_length=50)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=40)
    option3 = models.CharField(max_length=40)
    def __str__(self):
        return self.question

class Student(models.Model):
    name = models.CharField(max_length=30)
    mark = models.IntegerField()
    def __str__(self):
        return self.name

