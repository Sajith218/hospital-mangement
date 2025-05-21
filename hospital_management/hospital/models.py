from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        # Fallback to username if full name is not set
        return self.user.get_full_name() or self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)  # Patient's name
    age = models.IntegerField()              # Patient's age
    condition = models.TextField()           # Description of the patient's medical condition

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.appointment_date}"
