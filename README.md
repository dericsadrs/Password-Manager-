# Password Manager

A simple password manager GUI application built using Python and Tkinter. This program allows users to generate strong passwords and store them along with their associated websites and email addresses securely.

## Features

- Generate secure passwords with a combination of letters, numbers, and symbols.
- Store website credentials, including the website URL, associated email/username, and password.
- Retrieve saved passwords for specific websites.
- Option to show/hide the password while entering and viewing.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## How to Use

1. Clone the repository or download the source code.
2. Install the required dependencies if not already installed.
3. Run the `password_manager.py` script using Python: `python password_manager.py`.
4. The Password Manager GUI will open, allowing you to interact with the application.

## Usage

### Generate Password

1. Click the "Generate Password" button to generate a strong password.
2. The generated password will be displayed in the password entry field and copied to the clipboard.
3. The password will remain in the clipboard until you copy something else or exit the application.

### Save Password

1. Enter the website URL in the "Website" entry field.
2. Enter the associated email/username in the "Email/Username" entry field.
3. Enter the password for the website in the "Password" entry field.
4. Click the "Add" button to save the credentials securely.

### Find Password

1. Enter the website URL for which you want to retrieve the password in the "Website" entry field.
2. Click the "Search" button to find the saved credentials for the website.
3. The email/username and password for the specified website will be displayed in a popup dialog.

### Show/Hide Password

1. To toggle the visibility of the password in the "Password" entry field, click the "Show Password" button.

## Data Storage

- The saved website credentials are stored in a JSON file named `data.json`.
- The JSON file is automatically created in the same directory as the script if it does not exist.


# Attibutions
# <a href="https://www.flaticon.com/free-icons/lock" title="lock icons">Lock icons created by Pixel perfect - Flaticon</a>
