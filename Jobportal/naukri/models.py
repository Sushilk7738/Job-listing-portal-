from django.db import models

# Create your models here.

job_title = [
    ("Developer", "Developer"),
    ("Manager", "Manager"),
    ("Asst.Manager", "Asst.Manager"),
    ("HR", "HR"),
]

qual = [
    ("Bsc", "Bsc"),
    ("M.Tech", "M.Tech"),
    ("B.Tech", "B.Tech"),
    ("Msc", "Msc"),
]

class Mumbai(models.Model):
    company_name = models.CharField(max_length=25)
    job_title = models.CharField(max_length=20, choices=job_title)
    sal = models.FloatField()
    qualification = models.CharField(max_length=10, choices=qual)
    joining_date = models.DateField()
    location = models.CharField(max_length=25)
    address = models.CharField(max_length=200)

class Pune(models.Model):
    company_name = models.CharField(max_length=25)
    job_title = models.CharField(max_length=20, choices=job_title)
    sal = models.FloatField()
    qualification = models.CharField(max_length=10, choices=qual)
    joining_date = models.DateField()
    location = models.CharField(max_length=25)
    address = models.CharField(max_length=200)

class Bengaluru(models.Model):
    company_name = models.CharField(max_length=25)
    job_title = models.CharField(max_length=20, choices=job_title)
    sal = models.FloatField()
    qualification = models.CharField(max_length=10, choices=qual)
    joining_date = models.DateField()
    location = models.CharField(max_length=25)
    address = models.CharField(max_length=200)

