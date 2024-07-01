# Author: Apache X692 Attack Helicopter
# Created on: 01/07/2024
class EmployeeRepository:
    def __init__(self):
        self.employees = []

    def __len__(self):
        return len(self.employees)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.employees[key.start:key.stop:key.step]
        elif isinstance(key, int):
            if key < 0:
                key += len(self.employees)
            if key < 0 or key >= len(self.employees):
                raise IndexError("The index is out of bounds.")
            return self.employees[key]
        else:
            raise TypeError("Invalid argument type provided.")

    def __setitem__(self, key, value):
        self.employees[key] = value

    def __delitem__(self, key):
        del self.employees[key]

    def __str__(self):
        return '\n'.join(str(emp) for emp in self.employees)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.employees})"

    def add_employee(self, employee_data):
        self.employees.append(employee_data)

    def load_employees(self, employees_data):
        self.employees.extend(employees_data)

    def get_all_employees(self):
        return self.employees
