from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment
from .forms import AppointmentForm  # <-- Import your form

def home(request):
    return render(request, 'hospital/home.html')

def doctor_list(request):
    doctors = Doctor.objects.all()   # <-- Use the Doctor model for real data
    return render(request, 'hospital/doctor_list.html', {'doctors': doctors})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patient_list.html', {'patients': patients})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospital/appointment_list.html', {'appointments': appointments})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')  # Make sure this URL/view/template exists
    else:
        form = AppointmentForm()
    return render(request, 'hospital/book_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'hospital/appointment_success.html')