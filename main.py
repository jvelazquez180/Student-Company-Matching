import tkinter as tk
from tkinter import ttk
import sqlite3

class StudentMatchingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student-Company Matching System")
        self.root.geometry("600x400")
        
        self.create_database()
        self.create_main_menu()
    
    def create_database(self):
        self.conn = sqlite3.connect("matching_system.db")
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                gpa REAL,
                                attendance INTEGER)''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS companies (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                min_gpa REAL,
                                min_attendance INTEGER)''')
        
        self.conn.commit()
    
    def create_main_menu(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True)
        
        ttk.Label(frame, text="Student-Company Matching System", font=("Arial", 16)).pack(pady=10)
        
        ttk.Button(frame, text="Enter Student Data", command=self.open_student_entry).pack(pady=5)
        ttk.Button(frame, text="Set Company Criteria", command=self.open_company_setup).pack(pady=5)
        ttk.Button(frame, text="Generate Report", command=self.generate_report).pack(pady=5)
        ttk.Button(frame, text="Exit", command=self.root.quit).pack(pady=10)
    
    def open_student_entry(self):
        student_window = tk.Toplevel(self.root)
        student_window.title("Enter Student Data")
        student_window.geometry("400x300")
        
        ttk.Label(student_window, text="Student Name:").pack(pady=5)
        self.student_name_entry = ttk.Entry(student_window)
        self.student_name_entry.pack(pady=5)
        
        ttk.Label(student_window, text="GPA:").pack(pady=5)
        self.student_gpa_entry = ttk.Entry(student_window)
        self.student_gpa_entry.pack(pady=5)
        
        ttk.Label(student_window, text="Attendance (%):").pack(pady=5)
        self.student_attendance_entry = ttk.Entry(student_window)
        self.student_attendance_entry.pack(pady=5)
        
        ttk.Button(student_window, text="Save", command=self.save_student_data).pack(pady=10)
    
    def open_company_setup(self):
        company_window = tk.Toplevel(self.root)
        company_window.title("Set Company Criteria")
        company_window.geometry("400x250")
        
        ttk.Label(company_window, text="Company Name:").pack(pady=5)
        self.company_name_entry = ttk.Entry(company_window)
        self.company_name_entry.pack(pady=5)
        
        ttk.Label(company_window, text="Minimum GPA:").pack(pady=5)
        self.company_gpa_entry = ttk.Entry(company_window)
        self.company_gpa_entry.pack(pady=5)
        
        ttk.Label(company_window, text="Minimum Attendance (%):").pack(pady=5)
        self.company_attendance_entry = ttk.Entry(company_window)
        self.company_attendance_entry.pack(pady=5)
        
        ttk.Button(company_window, text="Save", command=self.save_company_data).pack(pady=10)
    
    def save_student_data(self):
        name = self.student_name_entry.get()
        gpa = float(self.student_gpa_entry.get())
        attendance = int(self.student_attendance_entry.get())
        
        self.cursor.execute("INSERT INTO students (name, gpa, attendance) VALUES (?, ?, ?)", (name, gpa, attendance))
        self.conn.commit()
        print("Student data saved.")
    
    def save_company_data(self):
        name = self.company_name_entry.get()
        min_gpa = float(self.company_gpa_entry.get())
        min_attendance = int(self.company_attendance_entry.get())
        
        self.cursor.execute("INSERT INTO companies (name, min_gpa, min_attendance) VALUES (?, ?, ?)", (name, min_gpa, min_attendance))
        self.conn.commit()
        print("Company criteria saved.")
    
    def generate_report(self):
        print("Generating Report...")  # Placeholder for report generation

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentMatchingApp(root)
    root.mainloop()
