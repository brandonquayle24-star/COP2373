
import inspect
import Brandon_Sentence_Counter

with open("Brandon_Sentence_Counter_design_doc.txt", "w") as doc:
    doc.write(f"# Technical Design Document: {Brandon_Sentence_Counter.__name__}\n\n")

    doc.write("# Name: Brandon Quayle\n")
    doc.write("# Date: October 25, 2026\n")
    doc.write("# Program Description: This program allows the user to enter a paragraph, separates and displays each individual sentence, including sentences beginning with numbers, and counts the total number of sentences.\n\n")

    for name, func in inspect.getmembers(
        Brandon_Sentence_Counter, inspect.isfunction
    ):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")

    doc.write(
        "# Link to your repository: "
        "https://github.com/brandonquayle24-star/COP2373\n"
    )

print("Complete")
