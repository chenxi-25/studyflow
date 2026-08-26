from datetime import datetime

print("Welcome to StudyFlow!")

modules = []
while True:
    try:

        number_of_modules = int(input("How many modules are you taking?"))

        if number_of_modules >= 0:
            break
        print("Please enter 0 or a positive number.")


    except ValueError:
        print("Please enter an integer")

for i in range(number_of_modules):
    module = input(f"Enter module {i + 1}: ")
    modules.append(module)

print()
print("Your modules:")

for module in modules:
    print("-", module)

tasks = []

while True:
    try:

        number_of_tasks = int(input("How many tasks do you have?"))

        if number_of_tasks >= 0:
            break
        print("Please enter 0 or a positive number.")
    except ValueError:
        print("Please enter an integer")

for i in range(number_of_tasks):
    task_name = input("Enter task name:")
    print("What module is this task for?\n")

    for index, module in enumerate(modules):
        print(index+1, module)

    print()

    while True:
        try:
            choice = int(input("Select module number: "))
            if 1 <= choice <= len(modules):
                break
            print("That module number does not exist. Please try again.")

        except ValueError:
            print("Please enter a number.")

    task_module = modules[choice-1]

    while True:
        task_deadline = input("Enter task deadline:")

        try:
            datetime.strptime(task_deadline, "%d/%m/%Y")
            break
        except ValueError:
            print("Please enter a valid date in DD/MM/YYYY format.")
        

    while True:
        try:
            task_hours = int(input("Enter the estimated hours needed for this task: "))
            if task_hours > 0:
                break
            print("That is not a valid number of hours, please re-enter.")

        except ValueError:
            print("Please enter an integer.")
   

    task = {
        "name": task_name,
        "module": task_module,
        "deadline": task_deadline,
        "hours": task_hours
    }

    tasks.append(task)
print()
print("Your tasks:\n")
for task in tasks:
    print(task["name"])
    print("Module:", task["module"])
    print("Deadline:", task["deadline"])
    print("Estimated hours:", task["hours"])
    print()