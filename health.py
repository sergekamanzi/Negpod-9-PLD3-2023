    # Check if all fields are filled
    if not name or not email or not password or not confirm_password:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return
