from django.db import models


# ---------------------------
# Book Model
# ---------------------------
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.title


# ---------------------------
# Address Model (One-to-Many with Students)
# ---------------------------
class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


# ---------------------------
# Student Model (Many-to-Many with Address)
# ---------------------------
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address)

    def __str__(self):
        return self.name


# ---------------------------
# Address2 Model (For Lab 9 Task)
# ---------------------------
class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


# ---------------------------
# Student2 Model (Many-to-Many with Address2)
# ---------------------------
class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2, related_name="students")

    def __str__(self):
        return self.name


# ---------------------------
# Image Upload Model
# ---------------------------from django.db import models

class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title
