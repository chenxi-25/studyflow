print("Welcome to StudyFlow!")

modules = []

number_of_modules = int(input("How many modules are you taking? "))

for i in range(number_of_modules):
    module = input(f"Enter module {i + 1}: ")
    modules.append(module)

print()
print("Your modules:")

for module in modules:
    print("-", module)

print()
print("Your modules:")
print("1. Algorithms")
print("2. Machine Learning")
print("3. Software Engineering")

print()
print("Upcoming tasks:")
print("1. Algorithms coursework")
print("2. Machine Learning assignment")