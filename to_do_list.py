import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

tasks = []   # Initialize an empty list to store tasks

# Function to add a new task to the task list
def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)    # Append the entered task to the tasks list
    print(f"Task {task} added to the list.")
    print()

# Function to list all current tasks
def listTask():
    if not tasks:
        print(Fore.BLUE + "There are no tasks currently.")
        print()
    else:
        print()
        print("Current Tasks: ")
        for index,task in enumerate(tasks): # Enumerate through the tasks list and print each task with its index
            print(f"Task #{index}.{task}")
        print()


# Function to delete a specific task from the task list
def deleteTask():
    listTask()

    try:
        taskToDelete = int(input("Enter the number of the task you want to delete: "))
        if taskToDelete >=0 and taskToDelete < len(tasks): # Check if the entered index is within the range of the tasks list
            tasks.pop(taskToDelete)   # Remove the task at the specified index
            print(f"Task {taskToDelete} has been removed.")
            print()
        else:
            print(Fore.RED + f"Task number was not found.")
            print()
    except:
        print(Fore.RED + "Invalid input, Please try again.")  # Catch non-integer inputs and inform the user
        print()

# Main program entry point
if __name__ == "__main__":
     print(Fore.MAGENTA + Style.BRIGHT + "Welcome to the To Do List...")
     print()

     # Start an infinite loop to continually prompt the user for actions
     while True:
         print(Fore.CYAN + Style.BRIGHT + "Please Select one of the following Options.")
         print(Fore.CYAN + Style.BRIGHT +"--------------------------------------------")
         print(Fore.CYAN +"1. Add a new task")
         print(Fore.CYAN +"2. Delete a task")
         print(Fore.CYAN +"3. List tasks")
         print(Fore.CYAN +"4. Quit")
         print()

         choice = input("Enter your choice (1 to 4 ) :")
         # Execute the corresponding function based on the user's choice
         if choice == "1":
             addTask()
         elif choice == "2":
             deleteTask()
         elif choice == "3":
             listTask()
         elif choice == "4":
              break
         else:
             print(Fore.RED + "Invalid input, Please try again.")
             print()
     print()
     print(Fore.MAGENTA + Style.BRIGHT +"Good Bye, Have a great Day! :)")