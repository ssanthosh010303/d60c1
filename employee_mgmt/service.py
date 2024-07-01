# Author: Apache X692 Attack Helicopter
# Created on: 01/07/2024
from datetime import datetime, date


class EmployeeService:
    def __init__(self, repository, data_handler):
        self.repository = repository
        self.data_handler = data_handler

    def add_employee(self, name, dob, phone, email):
        try:
            dob_date = datetime.strptime(dob, "%Y/%m/%d").date()
            age = (date.today() - dob_date).days // 365
            employee_data = {
                "name": name,
                "dob": dob,
                "phone": phone,
                "email": email,
                "age": age
            }

            self.repository.add_employee(employee_data)
            return "Employee added successfully."
        except ValueError:
            return "Error: Invalid date format, please use YYYY/MM/DD."

    def save_employees(self, file_type):
        try:
            employees_data = self.repository.get_all_employees()

            if not employees_data:
                return "No employees to save."

            self.data_handler.save_employee(file_type, employees_data)
            return f"Employees data saved in {file_type} format."
        except Exception as e:
            return f"Failed to save data: {e}"

    def load_employees(self, filename):
        try:
            employees_data = self.data_handler.load_from_excel(filename)

            self.repository.load_employees(employees_data)
            return "Employees loaded successfully."
        except Exception as e:
            return f"Error loading data: {e}"
