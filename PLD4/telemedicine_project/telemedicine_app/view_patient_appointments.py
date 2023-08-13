#!/usr/bin/python3

from telemedicine_app.patient_classes import Patient
from telemedicine_app.professional_classes import Professional

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
            if self.current_user:
                print("Current User:", self.current_user)
                self.view_patient_appointments()
            else:
                print("Please log in first.")
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")
