class Person:
    def __init__(self, name, age, gender, address, phone_number):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__address = address
        self.__phone_number = phone_number

    #Getters
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_gender(self):
        return self.__gender
    
    def get_address(self):
        return self.__address
    
    def get_phone_number(self):
        return self.__phone_number
    
    #Setters

    def set_name (self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_gender(self, gender):
        self.__gender = gender

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number


    #Display person's information

    def display_person_info(self):
        return (
            f"Name: {self.__name}\tAge: {self.__age}\tGender: {self.__gender}\t"
            f"Address: {self.__address}\tPhone Number: {self.__phone_number}\t"
        )
        

    #DERIVED CLASS
class Student(Person):
    def __init__(self, name, age, gender, address, phone_number, student_id, course):
        super().__init__(name, age, gender, address, phone_number)
        self.__student_id = student_id
        self.__course = course

    #Getters
    def get_student_id(self):
        return self.__student_id
    def get_course(self):
        return self.__course
    
    #Setters
    def set_student_id(self, student_id):
        self.__student_id = student_id
    
    def set_course(self, course):
        self.__course = course

    #Display student's information

    def display_student_info(self):
        return (
            f"{self.get_name()}\t{self.get_age()}\t{self.get_gender()}\t"
            f"{self.get_address()}\t{self.get_phone_number()}\t"
            f"{self.__student_id}\t{self.__course}"
        )
       