import inspect
import student_grades

with open("student_grades_design_doc.txt", "w") as doc:

    doc.write(f"# Technical Design Document: {student_grades.__name__}\n\n")

    doc.write("# Name: Brandon Quayle\n")
    doc.write("# Date: October 29, 2026\n")
    doc.write("# Program Description: This program allows an instructor "
              "to enter student names and three exam grades. "
              "The information is saved to a CSV file and then "
              "read and displayed in a formatted table.\n\n")

    for name, func in inspect.getmembers(
        student_grades, inspect.isfunction
    ):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")

    doc.write("# GitHub Repository Link:\n")
    doc.write("https://github.com/brandonquayle24-star/COP2373\n")

print("Technical Design Document created successfully!")
