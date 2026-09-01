from datetime import datetime

def calculate_task_score(task):
    deadline_date = datetime.strptime(task["deadline"], "%d/%m/%Y").date()

    today = datetime.now().date()
    
    days_remaining = (deadline_date - today).days
    if days_remaining <= 2:
        time_priority_count = 5
    elif days_remaining <= 7:
        time_priority_count = 3
    else:
        time_priority_count = 1

    if task["priority"] == "High":
        priority_count = 3
    elif task["priority"] == "Medium":
        priority_count = 2
    else:
        priority_count = 1

    priority_score = priority_count + time_priority_count

    return priority_score


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
        task_deadline = input("Enter task deadline in DD/MM/YYYY form:")

        try:
            deadline_date = datetime.strptime(task_deadline, "%d/%m/%Y")
            if deadline_date.date() >= datetime.now().date():
                break
            print("The deadline cannot be in the past.")

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

    while True:
        task_priority = input("Enter task priority: High, Medium or Low: ").strip().lower()

        if task_priority in ["high", "medium", "low"]:
            task_priority = task_priority.capitalize()
            break

        print("That is not a valid option. Please enter High, Medium or Low.")

    print()

    task = {
        "name": task_name,
        "module": task_module,
        "deadline": task_deadline,
        "hours": task_hours,
        "priority": task_priority,
    }

    tasks.append(task)
print()
print("Your tasks:\n")
for task in tasks:
    print(task["name"])
    print("Module:", task["module"])
    print("Deadline:", task["deadline"])
    print("Estimated hours:", task["hours"])
    print("Priority:", task["priority"])
    print()

#calculate each task's priority score
for task in tasks:
    priority_score = calculate_task_score(task)

    task["score"] = priority_score

#sort scores from highest to lowest
sorted_tasks = sorted(tasks, key=lambda task: task["score"], reverse =True)

#display recommended study order
print("\nRecommended study order\n")

for i, task in enumerate(sorted_tasks):
    print(i+1, task["name"])
    print("Module:", task["module"])
    print("Deadline:", task["deadline"])
    print("Priority:", task["priority"])
    print("Estimated:", task["hours"])
    print()
