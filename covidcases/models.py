from django.db import models

# Create your models here.4
class Country(models.Model):
    country_name = models.CharField(max_length=200)
    active_cases = models.IntegerField(default=0)
    dead_cases = models.IntegerField(default=0)

    def __str__(self):
        return self.country_name + ' ' + str(self.active_cases)


class Patients(models.Model):
    active = 'active'
    dead = 'dead'
    choices_list = [
        (active, 'Active'),
        (dead, 'Dead')
    ]
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=200)
    status = models.CharField(max_length = 6, choices = choices_list)

    def __str__(self):
        return self.patient_name + ' ' + self.status
class User(models.Model):
    username=models.CharField(max_length=200,primary_key=True)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.username + ' ' + self.password
