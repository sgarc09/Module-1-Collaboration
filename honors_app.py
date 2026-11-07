# Name: Stephanie Garcia Garcia
# File: honors_app.py
# Description: Accepts student last names, first names, and GPAs,
#              then determines whether each student qualifies for the Dean's List
#              (GPA >= 3.5) or the Honor Roll (GPA >= 3.25). Processing stops when
#              the last name 'ZZZ' is entered.

DEANS_LIST_MIN = 3.5
HONOR_ROLL_MIN = 3.25
SENTINEL = "ZZZ"


def get_gpa():
    """Keep asking until the user enters a valid float for the GPA."""
    while True:
        try:
            return float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid GPA. Please enter a number such as 3.42.")


def main():
    while True:
        last_name = input("\nEnter the student's last name (ZZZ to quit): ").strip()
        if last_name == SENTINEL:
            print("Finished processing student records.")
            break
 
        first_name = input("Enter the student's first name: ").strip()
        gpa = get_gpa()

        if gpa >= DEANS_LIST_MIN:
            print(f"{first_name} {last_name} (GPA {gpa:.2f}) has made the Dean's List.")
        elif gpa >= HONOR_ROLL_MIN:
            print(f"{first_name} {last_name} (GPA {gpa:.2f}) has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} (GPA {gpa:.2f}) did not make the Dean's List or Honor Roll.")


main()