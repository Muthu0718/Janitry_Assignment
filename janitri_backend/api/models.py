from django.db import models

# User Model (Django already provides a User model, but we will extend it)
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def _str_(self):
        return self.email

# Patient Model
class Patient(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patients")

    def _str_(self):
        return self.name

# HeartRate Model
class HeartRate(models.Model):
    rate = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="heart_rates")

    def _str_(self):
        return f"Heart rate: {self.rate} bpm at {self.timestamp}"