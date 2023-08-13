#!/usr/bin/python3

class Patient:
    def __init__(self, name):
        self.name = name
        self.role = "patient"
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def display_appointments(self):
        print("Your Appointments:")
        for appointment in self.appointments:
            print(f"Professional: {appointment['professional']}")
            print(f"Appointment Time: {appointment['appointment_time']}")
            print(f"Service Type: {appointment['service_type']}")
            print("----")
