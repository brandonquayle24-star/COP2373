import csv


def write_grades():
    """
    Function Name: write_grades
    Purpose: Collect student names and three exam grades
             and save the information to grades.csv.
    Parameters:
        None
    Variables:
        num_students (int): Number of students to enter.
        first_name (str): Student's first name.
        last_name (str): Student's last name.
        exam1 (int): First exam grade.
        exam2 (int): Second exam grade.
        exam3 (int): Third exam grade.
        file: CSV file used to store student records.
        writer: CSV writer object.
    Logic:
        1. Ask the instructor for the number of students.
        2. Open grades.csv using the with keyword.
        3. Write the column headers.
        4. Loop through each student.
        5. Collect the student's name and three grades.
        6. Write the student's information to the file.
    Return:
        None
    """
    num_students = int(input("How many students? "))

    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "First Name", "Last Name",
            "Exam 1", "Exam 2", "Exam3"
        ])

        for i in range(num_students):
            print(f"\nStudent {i + 1}")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            writer.writerow([
                first_name, last_name,
                exam1, exam2, exam3
            ])

    print("\nGrades saved to grades.csv")


def read_grades():
    """
    Function Name: read_grades
    Purpose: Read grades.csv and display student records
             in a formatted table.
    Parameters:
        None
    Variables:
        file: CSV file containing student grades.
        reader: CSV reader object.
        row (list): Each record read from the file.
    Logic:
        1. Open grades.csv using the with keyword.
        2. Create a CSV reader object.
        3. Read and display the column headers.
        4. Loop through the student records.
        5. Display each record in tabular format.
    Return:
        None
    """
    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)

        headers = next(reader)

        print("\nStudent Grades")
        print("-" * 65)

        print(
            f"{headers[0]:<15}{headers[1]:<15}"
            f"{headers[2]:<10}{headers[3]:<10}"
            f"{headers[4]:<10}"
        )

        print("-" * 65)

        for row in reader:
            print(
                f"{row[0]:<15}{row[1]:<15}"
                f"{row[2]:<10}{row[3]:<10}"
                f"{row[4]:<10}"
            )


def main():
    """
    Function Name: main
    Purpose: Run the student grade recording program.
    Parameters:
        None
    Variables:
        None
    Logic:
        1. Call write_grades to create the CSV file.
        2. Call read_grades to display the saved grades.
    Return:
        None
    """
    write_grades()
    read_grades()


if __name__ == "__main__":
    main()
