#importing student class from person.py
import csv

from person import Student

#Function to save student information to a file


def register_student(student):
    try:
        filename = "studentsInfo.csv"
    #     with open(filename, "a") as file:
    #         if file.tell() == 0:
    #             file.write("Name\tAge\tGender\tAddress\tPhone Number\tStudent ID\tCourse\n")

    #         file.write(
    #             f"{student.get_name()}\t{student.get_age()}\t{student.get_gender()}\t"
    #             f"{student.get_address()}\t{student.get_phone_number()}\t"
    #             f"{student.get_student_id()}\t{student.get_course()}\n"
    #         )
    #     return f"Student information saved successfully to {filename}"
    
    # except Exception as e:
    #     print(f"Error saving student information: {e}")
    #     return None
    
    # Check if the file exists and write headers if not
        file_exists = False
        try:
            with open(filename, "r") as file:
                file_exists = True
        except FileNotFoundError:
            pass
        
        # Append student data to the CSV file
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                # Write headers to the file
                writer.writerow(["Name", "Age", "Gender", "Address", "Phone Number", "Student ID", "Course"])
            
            # Write the student data
            writer.writerow([
                student.get_name(),
                student.get_age(),
                student.get_gender(),
                student.get_address(),
                student.get_phone_number(),
                student.get_student_id(),
                student.get_course()
            ])
        return f"Student information saved successfully to {filename}"
    
    except Exception as e:
        print(f"Error saving student information: {e}")
        return None

    #Function to add multiple students  records

def add_students_records():
    try:
        while True:
            #Enter student's information
            name = input("Enter student's name: ")
            age = input("Enter student's age: ")
            gender = input("Enter gender: ")
            address = input("Enter address: ")
            phone_number = input("Enter phone number: ")
            student_id = input("Enter student ID: ")
            course = input("Enter course: ")

            #Create student object
            student = Student(name, age, gender, address, phone_number, student_id, course)

            #Save student information to file
            message = register_student(student)
            print(message)

            # Ask if the user wants to add another record
            choice = input("Do you want to add another record? (yes/no): ").strip().lower()
            if choice != "yes":
                print("Exiting program. All records are saved.")
                break

            #Open the file to read the records
       # with open("studentsInfo.txt", "r") as file:
            #file.read()

    except Exception as e:
        print(f"Error adding student records: {e}")
        return None
    

#Call the function to add students records

if __name__ == "__main__":
    add_students_records()