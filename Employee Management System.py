# ==================  Employee Management System ========================================


employees = []

def add_employee():
  print('\n--- Add New Employee ---')
  emp_id = input('Enter Employee ID :')
  
  # check if the ID already exists
  for emp in employees:
    if emp['ID'] == emp_id:
      print('Employee ID already exists. Please try again.')
      return
  
# collect other details
  name = input("Enter Name: ")
  age = input("Enter Age: ")
  gender = input("Enter Gender: ")
  position = input("Enter Job Position: ")
  salary = input("Enter Salary: ")
  
  # Create dictionary and append the list
  new_employee = {
    'ID' : emp_id,
    'Name' : name,
    'Age' : age,
    'Gender' : gender,
    'Position' : position,
    'Salary' : salary
  }
  
  employees.append(new_employee)
  print('Employee added successfully')
  
  
def update_employee():
  print('\n--- Update Employee Details ---')
  emp_id = input('Enter Employee ID to update : ')
  # search for the employee
  for emp in employees:
    if emp['ID'] == emp_id:
      print('\n Which detail do you want to update?')
      print("1. Name")
      print("2. Age")
      print("3. Gender")
      print("4. Position")
      print("5. Salary")
      
      print()
      
      choice = input('Enter your choice (1-5) :')
      
      if choice == '1':
        print(f'Old Name : {emp['Name']}')
        emp['Name'] = input('Enter new Name : ')
        print('Name updated.')
        
      elif choice == '2':
        print(f'Old age : {emp['Age']}')
        emp['Age'] = input('Enter new Age : ')
        print('Age updated.')
        
      elif choice == '3':
        print(f'Old gender : {emp['Gender']}')
        emp['Gender'] = input('Enter new Gender : ')
        print('Gender updated.')
       
      elif choice == '4':
        print(f'Old Position : {emp['Position']}')
        emp['Position'] = input('Enter new Position : ')
        print('Position updated.')
      
      elif choice == '5':
        print(f'Old Salary : {emp['Salary']}')
        emp['Salary'] = input('Enter new Salary : ')
        print('Salary updated.')
      
      else:
         print('Invaild choice.')
        
      print('Employee updated successfully')
      return
    else:
      print('Employee not found')


def delete_employee():
  print('\n --- Delete Employee ---')
  
  emp_id = input('Enter Employee ID to delete : ')
  
  for emp in employees:
    if emp['ID'] == emp_id:
      employees.remove(emp)
      print('Employee deleted successfully.')
      return
    
print('Employee ID not found.')
    

def list_employees():
  print('\n-- Employee List ---')
  
  if not employees:
    print('No employee records found.')
    return
  
  print(f"{'ID':<10}{'Name':<10}{'Age':<10}{'Gender':<10}{'Position':<20}{'Salary':<10}")
  
  for emp in employees:
    print(f"{emp['ID']:<10}{emp['Name']:<10}{emp['Age']:<10}{emp['Gender']:<10}{emp['Position']:<20}{emp['Salary']:<10}")



while True:
  print('\n === Employee Management System ===')
  print("1. Add Employee")
  print("2. Update Employee")
  print("3. Delete Employee")
  print("4. List Employees")
  print("5. Exit")
  
  choice = input('Choose an option (1-5) :')
  
  if choice == '1':
    add_employee()
  elif choice == '2':
    update_employee()
  elif choice == '3':
    delete_employee()
  elif choice == '4':
    list_employees()
  elif choice == '5':
    print('Goodbye')
    break
  else:
    print('Invalid choice.')