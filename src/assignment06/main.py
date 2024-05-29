# ---------------------------------------------#
# Title: Assignment 06 -HR System
# Richard Khan 4/28/2024
#---------------------------------------------#

import csv
from prettytable import from_csv
from datetime import datetime

# Define the Data Constants
Menu: str =\
    '''
    Select from the following menu\n\
    1. Load employees in from the csv\n\
    2. Generate a report of all employees\n\
    3. Add a new employee\n\
    4. Generate a report of the current employees\n\
    5. Generate a report of employees who have recently left in the past 90 days\n\
    6. Generate a report of annual review reminders\n\
    7. Exit the program.
    '''
# Define data variables
menu_choice: str = ''
employee_id: str = ''
employee_name: str = ''
employee_address: str = ''
employee_ssn: str = ''
employee_dob: str = ''
employee_job_title: str = ''
employee_start_date: str = ''
employee_end_date: str = ''
employee_data: list = []
employees: list = []
active_employees: list = []
inactive_employees: list = []


# Define validation check variables
valid_input_flag: bool

def main():
    while True:

# Present the menu of choices
        print(Menu)
        menu_choice = str(input("Enter a menu option (1-7): "))

# Option 1: Load employees in from a CSV
        if menu_choice == "1":
            csvfile = open("employees.csv")
            employee_data = csv.reader(csvfile)
            for row in employee_data:
                print(', '.join(row))

# Generate a report of all employees
        if menu_choice == "2":
            with open("employees.csv") as fp:
                my_table = from_csv(fp)
                print(my_table)

# Option 3: Add a new employee
        if menu_choice == "3":
            print("You chose to add a new employee.")

            valid_input_flag = False
            while not valid_input_flag:
                employee_id = input("what is the employee ID?")
                # noinspection PyBroadException
                try:
                    employee_id = int(employee_id)
                    valid_input_flag = True
                except Exception:
                    print('Employee ID must be numeric.')
                    continue

            valid_input_flag = False
            while not valid_input_flag:
                name = input("what is the name (FirstName LastName)? ")
                # noinspection PyBroadException
                if employee_name.isalpha():
                    valid_input_flag = True

            valid_input_flag = False
            while not valid_input_flag:
                address = input("what is the address? ")
                # noinspection PyBroadException
                if employee_address.isalpha():
                    valid_input_flag = True

            valid_input_flag = False
            while not valid_input_flag:
                ssn = input("what is the ssn? ")
                # noinspection PyBroadException
                try:
                    ssn = int(ssn)
                    valid_input_flag = True
                except Exception:
                    print('Employee ssn must be numeric.')
                    continue

            valid_input_flag = False
            while not valid_input_flag:
                dob = input("what is the employee date of birth? ")
                # noinspection PyBroadException
                try:
                    dob = int(dob)
                    valid_input_flag = True
                except Exception:
                    print('Employee dob must be numeric')
                    continue

            valid_input_flag = False
            while not valid_input_flag:
                job_title = input("what is the job title? ")
                # noinspection PyBroadException
                if employee_job_title.isalpha():
                    valid_input_flag = True

            valid_input_flag = False
            while not valid_input_flag:
                start_date = input("what is the start date? ")
                # noinspection PyBroadException
                try:
                    start_date = int(start_date)
                    valid_input_flag = True
                except Exception:
                    print('Employee start date must be numeric.')
                    continue

            valid_input_flag = False
            while not valid_input_flag:
                end_date = input("what is the end date? ")
                # noinspection PyBroadException
                try:
                    end_date = int(end_date)
                    valid_input_flag = True
                except Exception:
                    print('Employee end date must be numeric.')
                    continue

            employee_data = [employee_id, name, address, ssn, dob, job_title, start_date, end_date]

            file = open('employees.csv', 'a', newline='')
            writer = csv.writer(file)
            writer.writerow(employee_data)
            file.close()

# Generate a report of all current employees
        if menu_choice == "4" or menu_choice == "5":

    # Get current date
            current_date = datetime.now().date()

    # Convert date strings to datetime objects
            for employee in employee_data:
                start_date = datetime.strptime(employee["start_date"], '%Y-%m-%dd').date()
                end_date = datetime.strptime(employee["end_date"], '%Y-%m-%d').date() if employee["end_date"] else None

                if end_date is None or employee_end_date >= current_date:
                    if start_date <= current_date:
                        active_employees.append(employee_data)
                    else:
                        inactive_employees.append(employee_data)
                else:
                    inactive_employees.append(employee_data)

            print("Active Employees:")
            for emp in active_employees:
                print(f" - {emp['name']} (Start: {emp['start_date']}, End: {emp['end_date']})")

            print("\nInactive Employees:")
            for emp in inactive_employees:
                print(f" - {emp['name']} (Start: {emp['start_date']}, End: {emp['end_date']})")



# Option 7: Exit program
if menu_choice == "7":
 print("Exiting")
 quit()

if __name__ == "__main__":
    main()

