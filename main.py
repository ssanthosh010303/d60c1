# Author: Apache X692 Attack Helicopter
# Created on: 01/07/2024
from employee_mgmt.repository import EmployeeRepository
from employee_mgmt.presentation import DataHandler
from employee_mgmt.service import EmployeeService


if __name__ == "__main__":
    repository = EmployeeRepository()
    data_handler = DataHandler()
    employee_service = EmployeeService(repository, data_handler)
    ui = EmployeeUI(employee_service)

    ui.run()
