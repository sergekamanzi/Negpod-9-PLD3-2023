mport tkinter as tk
from tkinter import messagebox

def register():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Check if all fields are filled
    if not name or not email or not password or not confirm_password:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    # You can add additional validation logic here if needed

    # Save the registration data to a file or database
    with open("registered_users.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}, Password: {password}\n")

    # Show a success message
    messagebox.showinfo("Success", "Registration successful!")

    # Clear the entry fields after successful registration
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Add form elements
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Label(root, text="Confirm Password:").pack()
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.pack()

# Add a register button
register_button = tk.Button(root, text="Register", command=register)
register_button.pack()

# Start the main event loop
root.mainloop()

