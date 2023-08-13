#!/usr/bin/python3

from datetime import datetime

class Professional:
    def __init__(self, name, id_card, phone_number, email, hospital, specialization, working_hours):
        self.name = name
        self.id_card = id_card
        self.phone_number = phone_number
        self.email = email
        self.hospital = hospital
        self.specialization = specialization
        self.working_hours = working_hours
        self.role = "professional"
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def is_available(self, appointment_time):
        try:
            appointment_datetime = datetime.strptime(appointment_time, "%Y-%m-%d %H:%M")
            working_start, working_end = map(lambda x: datetime.strptime(x, "%H:%M"), self.working_hours.split('-'))
            return working_start.time() <= appointment_datetime.time() <= working_end.time()
        except ValueError:
            return False

    def display_appointments(self):
        print("Your Appointments:")
        for appointment in self.appointments:
            print(f"Patient: {appointment['patient']}")
            print(f"Appointment Time: {appointment['appointment_time']}")
            print(f"Service Type: {appointment['service_type']}")
            print("----")
