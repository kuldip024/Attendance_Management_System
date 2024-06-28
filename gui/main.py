import tkinter as tk
from tkinter import messagebox
import subprocess

def run_create_database():
    subprocess.run(["python", "create_database.py"])

def run_register_user():
    subprocess.run(["python", "register_user.py"])

def run_take_attendance():
    subprocess.run(["python", "take_attendance.py"])

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Attendance System")

        self.label = tk.Label(root, text="Facial Recognition Attendance System", font=('Helvetica', 16, 'bold'))
        self.label.pack(pady=20)

        self.create_db_button = tk.Button(root, text="Create Database", command=run_create_database, width=25)
        self.create_db_button.pack(pady=10)

        self.register_user_button = tk.Button(root, text="Register User", command=run_register_user, width=25)
        self.register_user_button.pack(pady=10)

        self.take_attendance_button = tk.Button(root, text="Take Attendance", command=run_take_attendance, width=25)
        self.take_attendance_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
