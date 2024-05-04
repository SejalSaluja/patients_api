from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    blood_group = models.CharField(max_length=5)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
