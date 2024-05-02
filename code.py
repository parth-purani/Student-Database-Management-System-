#!/usr/bin/env python3
"""
Objective: This script acts as  a student database management system for an educational assignment. Its primary functions include adding, editing, dropping courses from, retrieving information about, and removing student records. 

These operations are facilitated through a command-line interface, with data validation and file-based persistence for storing student information.

The system allows users to interactively manage student details and course enrollments, updating a file (studentsDatabase.dat) to maintain a record of the student data.

"""
# Main function for student database management.
def main():
    # Display menu options.
    # write the contents of your main function here
    print("********************************************************")
    print("** Welcome to our students database system")
    # List of operations.
    print("** [a] to add new student record")
    print("** [e] to edit an existing student record")
    print("** [d] to drop a course for an existing student record")
    print("** [i] to get information about a student record")
    print("** [r] to remove an existing student record")
    print("** [q] to quit")

    #Load data from file
    database = {}
    with open("studentsDatabase.dat", "r") as database_file:
        for line in database_file:
            fields = line.strip().split(';')
            student_id = fields[0]
            database[student_id] = line.strip()
    # Main loop for user input handling
    while True:
        choice = input("******************************************************** Your choice: ").lower()
        if choice == "a": 
            # call the function to add a new student in the database.
            add(database)
        elif choice == "e":
            # call the function to edit the information of an existing student.
            edit(database)
        elif choice == "d":
            # call the function to drop a course for an existing student.
            drop(database)
        elif choice == "r":
            # call the function to remove the record of an existing student
            remove(database)
        elif choice == "i":
        # call the function to display the information of an existing student.
            info(database)
        elif choice == "q":
            break # quit the program
        else:
             print("Invalid choice, please enter a valid choice!")

# define your functions here.
def add(database):
    while True:
        #checking the condition
        student_id = input("Please enter student Id: ") #asking the details
        student_name = input("Please enter student name: ")
        student_semester = input("Please enter student semester: ")
        student_email = input("Please enter student email: ")
        while True: #asking codes list which is speperated by comma
            course_codes = input("Please enter comma-separated course codes list: ").upper().split(',')

            # Validate course codes
            valid_course_codes = []
            invalid_course_codes = []
            #for loop for courses and with digit and alpha functions
            for course_code in course_codes:
                if len(course_code) != 6 or not course_code[:3].isalpha() or not course_code[3:].isdigit():
                    invalid_course_codes.append(course_code)

            if invalid_course_codes: #checking if the course wrong then invalid prompt
                print(f"The following course codes are invalid: {', '.join(invalid_course_codes)}. Please enter all course codes again.")
                continue
            elif len(course_codes) < 1 or len(course_codes) > 5:
                print("Invalid number of course codes. You should enter between 1 and 5 course codes.")
                continue
            else:
                valid_course_codes = course_codes
                break#assigning codes to valid

        # Validate semester format
        if not student_semester.startswith('S') or not student_semester[1:].isdigit() or int(student_semester[1:]) < 1 or int(student_semester[1:]) > 8:
            print("Invalid semester format. Semester should be in the format S1, S2, ..., S8.")
            continue

        # Check if the student ID already exists in the database
        if student_id in database:
            print("A student with this ID already exists.")
            choice = input("Do you want to try a new ID (Y/N)? ").strip().lower()
            if choice == 'y':
                continue
            else:
                break

        # Add the student record to the database
        new_record = student_name + ";" + student_id + ";" + student_semester + ";" + student_email + ";" + ",".join(valid_course_codes)
        database[student_id] = new_record

        # Update the file with the new record
        with open("studentsDatabase.dat", "a") as database_file:
            database_file.write("\n" + new_record)

        print("Record added successfully!")
        break
#edit fucntion with database argument passed
def edit(database):
    while True:#if true then it will modify the email and the semester
        student_id, student_info, course_codes = info(database)
        if student_id is None:
            break

        field_choice = input("\nWhich field do you want to edit? [S] for Semester or [E] for Email address: ").strip().lower()

        if field_choice == 's':
            new_semester = input("Enter the new value for semester: ")
            student_info[2] = new_semester

            # Join the updated student_info list into a string
            updated_record = ';'.join(student_info)

            # Update the student's record in the database
            database[student_id] = updated_record

            # Update the database file with the new record
            with open("studentsDatabase.dat", "w") as database_file:
                for student_id, student_info in database.items():
                    database_file.write(student_info + "\n")

            print("Record updated successfully!")
            return
        elif field_choice == 'e':
            new_email = input("Enter the new value for email address: ")
            student_info[3] = new_email

            # Join the updated student_info list into a string
            updated_record = ';'.join(student_info)

            # Update the student's record in the database
            database[student_id] = updated_record

            # Update the database file with the new record
            with open("studentsDatabase.dat", "w") as database_file:
                for student_id, student_info in database.items():
                    database_file.write(student_info + "\n")

            print("Record updated successfully!")
            return
        else:
            print("Invalid choice. Please select [S] for Semester or [E] for Email address.")
#drop fucntion for dropping the course
def drop(database):
    while True:
        student_id, student_info, course_codes = info(database)

        if student_id is None:
            break

        while True:#which course has to be dropped
            course_to_drop = input("Please enter the course code you want to drop: ").strip().upper()

            # Check if the course exists in the student's course list
            if course_to_drop not in [code.strip() for code in course_codes]:
                print("This course is not in the student's course list.")
                choice = input("Press [n] to try a new course code or [m] for the main menu: ").strip().lower()
                if choice == 'n':
                    continue  # Try a new course code
                elif choice == 'm':
                    return  # Return to the main menu
                else:
                    print("Invalid choice. Returning to the main menu.")
                    return
            else:
                # Confirm with the admin
                confirmation = input("Are you sure you want to remove course " + str(course_to_drop) + " for this student? (Y/N): ").strip().lower()
                if confirmation == 'y':
                    # Remove the course from the student's course list
                    course_codes = [code.strip() for code in course_codes]
                    course_codes.remove(course_to_drop)

                    # Join the updated course_codes list into a string
                    updated_course_codes = ', '.join(course_codes)

                    # Update the student's record in the database
                    student_info[4] = updated_course_codes

                    # Join the updated student_info list into a string
                    updated_record = ';'.join(student_info)

                    # Update the student's record in the database
                    database[student_id] = updated_record

                    # Update the database file with the new record
                    with open("studentsDatabase.dat", "w") as database_file:
                        for student_id, student_info in database.items():
                            database_file.write(student_info + "\n")

                    print("Course " + str(course_to_drop) + " removed successfully!")
                    return
                elif confirmation == 'n':
                    print("Course " + str(course_to_drop) + " not removed.")
                    return  # Return to the main menu
                else:
                    print("Invalid choice. Returning to the main menu.")
                    return
#remove fucntion which removes every stuff
def remove(database):
    while True:
        student_id, student_info, _ = info(database)

        if student_id is None:
            break

        # Confirm with the user
        confirmation = input(f"Are you sure you want to remove the student with ID " + str(student_id) +"? (Y/N): ").strip().lower()
        if confirmation == 'y':
            # Remove the student record from the database
            del database[student_id]

            # Update the database file without blank lines
            with open("studentsDatabase.dat", "w") as database_file:
                for student_info in database.values():
                    database_file.write(student_info + "\n")

            print("Student with ID " + str(student_id) +" removed successfully!")
            return
        elif confirmation == 'n':
            print("Student with ID " + str(student_id) +" not removed.")
            return  # Return to the main menu
        else:
            print("Invalid choice. Returning to the main menu.")
            return
#info function for the infirmation of every student as select below
def info(database):
    while True:
        student_id = input("Please enter student Id: ")
        # Check if the student ID exists in the database
        if student_id not in database:
            print("This ID does not exist.")
            choice = input("Press [n] to try a new ID or [m] for the main menu: ").strip().lower()
            if choice == 'n':
                continue  # Try a new ID
            elif choice == 'm':
                return None, None, None
            else:
                print("Invalid choice. Returning to the main menu.")
                return None, None, None

        student_info = database[student_id].split(';')
        student_name = student_info[0]
        student_semester = student_info[2]
        student_email = student_info[3]
        course_codes = student_info[4].split(',')
#printing all the details as requested
        print("The following is the student information:")
        print("Name:", student_name)
        print("ID:", student_id)
        print("Semester:", student_semester)
        print("Email:", student_email)
        print("\nCourse Codes:", ', '.join(course_codes))
        return student_id, student_info, course_codes

if __name__ == "__main__":
    main()#main function
