# Load records from file

def load_data():
    students = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                students[name] = float(score)
    return students

# Save records to file

def save_data(students):
    with open(FILE_NAME, "w") as file:
        for name, score in students.items():
            file.write(f"{name},{score}\n")

# Add student

def add_student(students):
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists!")
        return
    score = float(input("Enter score: "))
    students[name] = score
    print("Student added successfully!")

# View all students

def view_students(students):
    if not students:
        print("No records found.")
        return
    print("\n--- Student Scores ---")
    for name, score in students.items():
        print(f"{name}: {score}")

# Update student score

def update_student(students):
    name = input("Enter student name to update: ")
    if name in students:
        score = float(input("Enter new score: "))
        students[name] = score
        print("Score updated!")
    else:
        print("Student not found.")

# Delete student

def delete_student(students):
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted!")
    else:
        print("Student not found.")

# Calculate statistics

def calculate_stats(students):
    if not students:
        print("No data available.")
        return
    
    scores = list(students.values())
    avg = sum(scores) / len(scores)
    high = max(scores)
    low = min(scores)

    print("\n--- Statistics ---")
    print(f"Average Score: {avg:.2f}")
    print(f"Highest Score: {high}")
    print(f"Lowest Score: {low}")

# Main program

def main():
    students = load_data()

    while True:
        print("\n===== Student Score Tracker =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Score")
        print("4. Delete Student")
        print("5. Calculate Statistics")
        print("6. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            calculate_stats(students)
        elif choice == "6":
            save_data(students)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()