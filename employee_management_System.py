class Employee:
    def __init__(self, name, phone, ssn, email, salary):
        self.name = name
        self.ssn = ssn
        self.phone = phone
        self.email = email
        self.salary = salary

    def display_info(self):
        print("----------------------------", self.name, "-----------------------------")
        print("SSN:", self.ssn)
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Salary: Rs." + str(self.salary))
        print("------------------------------------------------------------------------")


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_all_employees(self):
        if not self.employees:
            print("No employees in the system.")
        else:
            for employee in self.employees:
                employee.display_info()

    def search_employee_by_ssn(self, ssn):
        for employee in self.employees:
            if employee.ssn == ssn:
                employee.display_info()
                return
        print("Employee with SSN", ssn, "not found.")

    def edit_employee_information(self, ssn):
        for employee in self.employees:
            if employee.ssn == ssn:
                print("Editing information for", employee.name)
                employee.phone = input("Enter new phone number: ")
                employee.email = input("Enter new email: ")
                employee.salary = float(input("Enter new salary: "))
                print("Employee information updated.")
                return
        print("Employee with SSN", ssn, "not found.")

    def total_employee(self):
        total = len(self.employees)
        print("Total Employees are:", total)

    def total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        print("Total salary of all employees is: Rs.", total)


def add_employee_to_system(emp_sys):
    name = input("\nEnter Employee Name (less than 15 characters): ")
    while len(name) > 15:
        name = input("\nName too long! Enter Employee Name (less than 15 characters): ")

    phone = input("Enter 11-digit phone number: ")
    while len(phone) != 11 or not phone.isdigit():
        phone = input("Invalid phone number! Enter an 11-digit phone number: ")

    ssn = input("Enter 5-digit SSN number: ")
    while len(ssn) != 5 or not ssn.isdigit():
        ssn = input("Invalid SSN! Enter a 5-digit SSN number: ")

    email = input("Enter email (e.g., wajdan@gmail.com): ")
    while "@" not in email or "." not in email:
        email = input("Invalid email! Enter a valid email (e.g., wajdan@gmail.com): ")

    while True:
        try:
            salary = float(input("Enter salary in numbers: "))
            break
        except ValueError:
            print("Invalid input! Please enter salary in numbers.")

    emp = Employee(name, phone, ssn, email, salary)
    emp_sys.add_employee(emp)
    print("Employee added successfully!")


def main():
    emp_sys = EmployeeManagementSystem()

    while True:
        print("\n1: Add Employee")
        print("2: View all Employees")
        print("3: Search employee by SSN")
        print("4: Edit employee information")
        print("5: Total Employees")
        print("6: Total Salary of all Employees")
        print("7: Exit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid input! Please enter a valid choice.")
            continue

        if choice == 7:
            break
        elif choice == 1:
            add_employee_to_system(emp_sys)
        elif choice == 2:
            emp_sys.view_all_employees()
        elif choice == 3:
            ssn = input("Enter SSN number: ")
            while len(ssn) != 5 or not ssn.isdigit():
                ssn = input("Invalid SSN! Enter a 5-digit SSN number: ")
            emp_sys.search_employee_by_ssn(ssn)
        elif choice == 4:
            ssn = input("Enter SSN number: ")
            while len(ssn) != 5 or not ssn.isdigit():
                ssn = input("Invalid SSN! Enter a 5-digit SSN number: ")
            emp_sys.edit_employee_information(ssn)
        elif choice == 5:
            emp_sys.total_employee()
        elif choice == 6:
            emp_sys.total_salary()
        else:
            print("You chose an invalid option!")


if __name__ == "__main__":
    main()
