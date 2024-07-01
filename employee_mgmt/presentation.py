# Author: Apache X692 Attack Helicopter
# Created on: 01/07/2024
class EmployeeUI:
    def __init__(self, employee_service):
        self.employee_service = employee_service

    def run(self):
        options = {
            '1': self.input_employee_details,
            '2': self.bulk_load_from_excel,
            '3': self.save_employees
        }

        while True:
            print("\n1. Enter Employee Details")
            print("2. Load Employees from Excel")
            print("3. Save Employees")
            print("4. Exit")

            choice = input("Choose an option: ")
            action = options.get(choice)

            if choice == '4':
                print("Exiting...")
                break
            elif action:
                print(action())
            else:
                print("Invalid option, please try again.")

    def input_employee_details(self):
        name = input("Enter name: ")
        dob = input("Enter DoB (YYYY/MM/DD): ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        return self.employee_service.add_employee(name, dob, phone, email)

    def bulk_load_from_excel(self):
        filename = input("Enter Excel file name: ")

        return self.employee_service.load_employees(filename)

    def save_employees(self):
        file_type = input("Choose file type (text/excel/pdf): ")

        return self.employee_service.save_employees(file_type)
