from datetime import datetime

class TelemedicinePlatform:
    def __init__(self):
        self.patients = []
        self.professionals = []
        self.appointments = []
        self.current_user = None

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")

            if choice == '1':
                self.register_patient()
            elif choice == '2':
                self.register_professional()
            elif choice == '3':
                self.login()
            elif choice == '4':
                if self.current_user:
                    self.book_appointment()
                else:
                    print("Please log in first.")
            elif choice == '5':
                self.display_registered_patients()
            elif choice == '6':
                if self.current_user:
                    self.display_appointments()
                else:
                    print("Please log in first.")
            elif choice == '7':
                self.login_professional()
            elif choice == '8':
                self.view_patient_appointments()
            elif choice == '9':
                break
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        print("---- Telemedicine Platform Menu ----")
        print("1. Register as a Patient")
        print("2. Register as a Healthcare Professional")
        print("3. Login")
        print("4. Book an Appointment")
        print("5. View Registered Patients")
        print("6. View Appointments")
        print("7. Login as a Healthcare Professional")
        print("8. View Patient Appointments")
        print("9. Exit")

    def register_patient(self):
        name = input("Name: ")
        id_card = input("ID Card: ")
        phone_number = input("Phone Number: ")
        email = input("Email (optional): ")
        age = input("Age: ")

        patient = {
            "name": name,
            "id_card": id_card,
            "phone_number": phone_number,
            "email": email,
            "age": age,
            "role": "patient"
        }
        self.patients.append(patient)
        print("Patient registered successfully.")

    def register_professional(self):
        name = input("Name: ")
        id_card = input("ID Card: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        hospital = input("Hospital: ")
        specialization = input("Specialization: ")
        working_hours = input("Working Hours (HH:MM-HH:MM): ")

        professional = {
            "name": name,
            "id_card": id_card,
            "phone_number": phone_number,
            "email": email,
            "hospital": hospital,
            "specialization": specialization,
            "working_hours": working_hours,
            "role": "professional"
        }
        self.professionals.append(professional)
        print("Healthcare professional registered successfully.")

    def login(self):
        phone_number = input("Phone Number: ")
        for user in self.patients + self.professionals:
            if user["phone_number"] == phone_number:
                self.current_user = user
                print(f"Logged in as {user['name']}.")
                return
        print("User not found.")

    def book_appointment(self):
        print("Available Healthcare Professionals:")
        for i, professional in enumerate(self.professionals):
            print(f"{i + 1}. {professional['name']} ({professional['specialization']})")

        choice = int(input("Select a healthcare professional: ")) - 1
        if 0 <= choice < len(self.professionals):
            professional = self.professionals[choice]

            print(f"Working Hours for {professional['name']}: {professional['working_hours']}")
            appointment_time = input("Appointment Time (YYYY-MM-DD HH:MM): ")
            service_type = input("Service Type (online or in-person): ")
            payment_method = input("Payment Method: ")

            if self.is_valid_appointment_time(appointment_time, professional):
                appointment = {
                    "patient": self.current_user['name'],
                    "professional": professional['name'],
                    "appointment_time": appointment_time,
                    "service_type": service_type,
                    "payment_method": payment_method
                }
                self.appointments.append(appointment)
                print("Appointment booked successfully.")
            else:
                print(f"start again you are not registered as Doctor is available between {professional['working_hours']}.")
        else:
            print("Invalid choice.")

    def is_valid_appointment_time(self, appointment_time, professional):
        try:
            appointment_datetime = datetime.strptime(appointment_time, "%Y-%m-%d %H:%M")
            working_start, working_end = map(lambda x: datetime.strptime(x, "%H:%M"), professional['working_hours'].split('-'))
            return working_start.time() <= appointment_datetime.time() <= working_end.time()
        except ValueError:
            return False

    def display_registered_patients(self):
        print("Registered Patients:")
        for i, patient in enumerate(self.patients):
            print(f"{i + 1}. {patient['name']}")

    def display_appointments(self):
        print("Your Appointments:")
        for appointment in self.appointments:
            if appointment["patient"] == self.current_user['name']:
                print(f"Professional: {appointment['professional']}")
                print(f"Appointment Time: {appointment['appointment_time']}")
                print(f"Service Type: {appointment['service_type']}")
                print("----")

    def login_professional(self):
        phone_number = input("Phone Number (Healthcare Professional): ")
        for user in self.professionals:
            if user["phone_number"] == phone_number:
                self.current_user = user
                print(f"Logged in as {user['name']} (Healthcare Professional).")
                return
        print("Healthcare Professional not found.")

    def view_patient_appointments(self):
        if self.current_user and self.current_user['role'] == 'professional':
            print("Your Appointments:")
            for appointment in self.appointments:
                if appointment["professional"] == self.current_user['name']:
                    print(f"Patient: {appointment['patient']}")
                    print(f"Appointment Time: {appointment['appointment_time']}")
                    print(f"Service Type: {appointment['service_type']}")
                    print("----")
        else:
            print("You do not have the permissions to view appointments.")

# Instantiate and run the platform
if __name__ == "__main__":
    platform = TelemedicinePlatform()
    platform.run()
