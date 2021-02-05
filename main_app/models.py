from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    location = models.CharField(max_length=100, blank=True)
    hourly_rate = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location}"
    

class Equipment(models.Model):
    model = models.CharField(max_length=100, blank=False)
    make = models.CharField(max_length=100, blank=True)
    mfg_year = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    mileage = models.PositiveIntegerField()
    hours = models.PositiveIntegerField()
    img_url = models.URLField(max_length=200, blank=True)
    cost = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make} {self.model}"


class Task(models.Model):
    task_name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    interval = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    instructions = models.TextField(blank=True)
    video = models.URLField(max_length=200, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task_name}"

class Tool(models.Model):
    tool_name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    img_url = models.URLField(max_length=200, blank=True)
    task = models.ManyToManyField(Task)

    def __str__(self):
        return f"{self.tool_name}"


class Consumables(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    part_number = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=100, blank=True)
    cost = models.PositiveIntegerField() 
    task = models.ManyToManyField(Task)

    def __str__(self):
        return f"{self.name}"


class Maint_Record(models.Model):
    date = models.DateField(auto_now=True)
    mileage = models.PositiveIntegerField() 
    hours = models.PositiveIntegerField() 
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"
