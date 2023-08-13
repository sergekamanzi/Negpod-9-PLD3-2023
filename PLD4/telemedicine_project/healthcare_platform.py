#!/usr/bin/python3


from datetime import datetime
from telemedicine_app.telemedicine_classes import TelemedicinePlatform  # Import the TelemedicinePlatform class

if __name__ == "__main__":
    platform = TelemedicinePlatform()
    while True:
        platform.display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            platform.register_patient()
        elif choice == '2':
            platform.register_professional()
        elif choice == '3':
            platform.login()
        elif choice == '4':
            if platform.current_user:
                platform.book_appointment()
            else:
                print("Please log in first.")
        elif choice == '5':
            platform.display_registered_patients()
        elif choice == '6':
            if platform.current_user:
                platform.display_appointments()
            else:
                print("Please log in first.")
        elif choice == '7':
            platform.login_professional()
        elif choice == '8':
            platform.view_patient_appointments()
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")
