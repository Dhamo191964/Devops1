import csv

def display_data():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")

    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, course, marks])

while True:
    print("\n1. View Data\n2. Add Student\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        display_data()
    elif choice == '2':
        add_student()
    elif choice == '3':
        break
    else:
        print("Invalid choice")
