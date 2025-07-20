# Step 1: Initial Sample Employee Data
employee_data = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Riya', 'age': 30, 'department': 'IT', 'salary': 70000}
}

# Step 3: Add Employee Function
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employee_data:
            print("Employee ID already exists. Please enter a unique ID.")
            return
        
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employee_data[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print("Employee added successfully!\n")
    except ValueError:
        print("Invalid input! Please try again.\n")

# Step 4: View All Employees
def view_employees():
    if not employee_data:
        print("No employees available.\n")
        return

    print("\n{:<10} {:<15} {:<10} {:<15} {:<10}".format("ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)
    for emp_id, details in employee_data.items():
        print("{:<10} {:<15} {:<10} {:<15} {:<10}".format(
            emp_id, details['name'], details['age'], details['department'], details['salary']))
    print()

# Step 5: Search Employee by ID
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employee_data:
            details = employee_data[emp_id]
            print("\nEmployee Details:")
            print(f"ID        : {emp_id}")
            print(f"Name      : {details['name']}")
            print(f"Age       : {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary    : {details['salary']}\n")
        else:
            print("Employee not found.\n")
    except ValueError:
        print("Invalid ID entered. Please try again.\n")

# Step 2 & 6: Main Menu Function
def main_menu():
    while True:
        print("========== Employee Management System ==========")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.\n")

# Start the Program
if __name__ == "__main__":
    main_menu()
