import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json



# Attibutions
# <a href="https://www.flaticon.com/free-icons/lock" title="lock icons">Lock icons created by Pixel perfect - Flaticon</a>

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

class PasswordManager:
    def __init__(self):
        self.setup_gui()


    def setup_gui(self):
        self.window = tk.Tk()
        self.window.title("Modified Password Manager")
        self.window.config(padx=50, pady=50)

        self.canvas = tk.Canvas(height=200, width=200)
        self.logo_img = tk.PhotoImage(file="logo.png")
        self.canvas.create_image(70, 70, image=self.logo_img)
        self.canvas.grid(row=0, column=1)

        

        # Labels
        self.website_label = tk.Label(text="Website:")
        self.website_label.grid(row=1, column=0)
        self.email_label = tk.Label(text="Email/Username:")
        self.email_label.grid(row=2, column=0)
        self.password_label = tk.Label(text="Password:")
        self.password_label.grid(row=3, column=0)

        # Entries
        self.website_entry = tk.Entry(width=21)
        self.website_entry.grid(row=1, column=1)
        self.website_entry.focus()
        self.email_entry = tk.Entry(width=35)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        self.email_entry.insert(0, "deric@gmail.com")
        self.password_entry = tk.Entry(width=21, show='*')
        self.password_entry.grid(row=3, column=1)

        # Buttons
        self.search_button = tk.Button(text="Search", width=13, command=self.find_password)
        self.search_button.grid(row=1, column=2)
        self.generate_password_button = tk.Button(text="Generate Password", command=self.generate_password)
        self.generate_password_button.grid(row=3, column=2)
        self.add_button = tk.Button(text="Add", width=36, command=self.save)
        self.add_button.grid(row=4, column=1, columnspan=2)

        # Show/Hide Password Button
        self.show_password_button = tk.Button(text="Show Password", command=self.toggle_password)
        self.show_password_button.grid(row=3, column=3)

        # Password label to display generated password
        self.generated_password_label = tk.Label(text="", font=("Arial", 10), fg="gray")
        self.generated_password_label.grid(row=3, column=4)

        self.clear_button = tk.Button(text="Clear", width=13, command=self.clear_fields)
        self.clear_button.grid(row=4, column=3)

        self.update_button = tk.Button(text="Update", width=13, command=self.update_password)
        self.update_button.grid(row=1, column=3)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.window.mainloop()

    # Password Generator Project
    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)

        password = "".join(password_list)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.generated_password_label.config(text="", fg="gray")
        pyperclip.copy(password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def save(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                self.website_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
                self.generated_password_label.config(text="", fg="gray")

    # ---------------------------- FIND PASSWORD ------------------------------- #
    def find_password(self):
        website = self.website_entry.get()
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

    # Show/Hide Password Function
    def toggle_password(self):
        if self.show_password_button["text"] == "Show Password":
            self.password_entry.config(show="")
            self.show_password_button["text"] = "Hide Password"
        else:
            self.password_entry.config(show="*")
            self.show_password_button["text"] = "Show Password"


     # ---------------------------- CLEAR ENTRY FIELDS -------------------------------
    def clear_fields(self):
        self.website_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    # ---------------------------- VIEW ALL PASSWORDS -------------------------------
    def view_all_passwords(self):
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if data:
                passwords_text = ""
                for website, details in data.items():
                    passwords_text += f"Website: {website}\nEmail: {details['email']}\nPassword: {details['password']}\n\n"
                messagebox.showinfo(title="All Passwords", message=passwords_text)
            else:
                messagebox.showinfo(title="Empty", message="No passwords saved yet.")

    # ---------------------------- CONFIRMATION ON EXIT -------------------------------
    def on_close(self):
        confirm_exit = messagebox.askyesno(title="Confirm Exit", message="Do you want to exit the Password Manager?")
        if confirm_exit:
            self.window.destroy()
 

    # ---------------------------- UPDATE PASSWORD -------------------------------
    def update_password(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                messagebox.showinfo(title="Error", message="No Data File Found.")
            else:
                if website in data:
                    confirm_update = messagebox.askyesno(title="Confirm Update",
                                                         message=f"Do you want to update the credentials for {website}?")
                    if confirm_update:
                        data[website]["email"] = email
                        data[website]["password"] = password
                        with open("data.json", "w") as data_file:
                            json.dump(data, data_file, indent=4)
                        messagebox.showinfo(title="Success", message="Password updated successfully.")
                else:
                    messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

    # ---------------------------- SAVE TO FILE -------------------------------
    def save_to_file(self):
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt",
                                                       filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, "w") as file:
                    for website, details in data.items():
                        file.write(f"Website: {website}\nEmail: {details['email']}\nPassword: {details['password']}\n\n")
                messagebox.showinfo(title="Success", message="Credentials saved to file.")

    # ---------------------------- LOAD FROM FILE -------------------------------
    def load_from_file(self):
        file_path = tk.filedialog.askopenfilename(defaultextension=".txt",
                                                  filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                credentials = file.read()
                messagebox.showinfo(title="Loaded Credentials", message=credentials)

    # ---------------------------- AUTO-COPY TO CLIPBOARD -------------------------------

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo(title="Success", message="Password copied to clipboard.")


# Create an instance of the PasswordManager class
if __name__ == "__main__":
    password_manager = PasswordManager()
