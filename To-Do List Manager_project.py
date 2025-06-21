# To-Do List Manager using python

# This program lets the user add, view, and delete tasks using a menu system


# Create an empty list to store the tasks
tasks = []

# Function to add a new task
def add_task():
  task = input('Enter a new task : ')
  tasks.append(task)
  print('Task added successfully')

# Function to view all tasks
def view_task():
  if tasks:
    print('Your tasks')
    # loop through the list with task number starting from 1
    for i , task in enumerate(tasks, start=1):
      print(f'{i}. {task}')
  else:
    # if the list is empty
    print('Your task list is empty')
    

# Function to delete a task
def delete_task():
  # show the task first
  view_task()
  task_index = int(input('Enter the task number to delete  :'))-1
  if 0 <= task_index < len(tasks):
    delete_task = tasks.pop(task_index)
    print(f'Deleted task : {delete_task}')
  else:
    print('Invalid task number')
  
# Main loop to display the menu and task user input continuously.
while True:
   print("\n-- To-Do List Manager --")
   print("1. Add Task")
   print("2. View Tasks")
   print("3. Delete Task")
   print("4. Exit")
  
# Ask user to choose an option
   choice = input('Enter your choice (1-4):')

# Based on choice, call the corresponding function
   if choice == '1':
      add_task()
   elif choice =='2':
     view_task()
   elif choice == '3':
     delete_task()
   elif choice =='4':
    #  Exit the loop
    print('Goodbye')
    break
   else:
    print('Invaild choice. Please try again.')
  

  