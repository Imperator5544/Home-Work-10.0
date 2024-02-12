"""
Створити ієрархію класів для опису академії.

Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.

Продумати архітектуру: реалізувати принципи ООП
"""

class Person:
    def __init__(self, name, birth=None):
        self.name = name
        self.birth = birth

        if not isinstance(birth, (str, type(None))):
            raise TypeError("Invalid birth format. Should be a string or None.")

class Teacher(Person):
    def __init__(self, name, birth, discipline):
        super().__init__(name, birth)
        self.discipline = discipline

    def show_info(self):
        print(f"Discipline: {self.discipline}")

class Student(Person):
    def __init__(self, name, birth, faculty):
        super().__init__(name, birth)
        self.faculty = faculty

    def show_info(self):
        print(f"Faculty: {self.faculty}")

class Academy:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates

    def show_info(self):
        print(f"Academy: {self.coordinates}")

class College(Academy):
    def __init__(self, name, coordinates, education):
        super().__init__(name, coordinates)
        self.education = education

    def show_info(self):
        print(f"College: {self.education}")

class School(Academy):
    def __init__(self, name, coordinates, number):
        super().__init__(name, coordinates)
        self.number = number

    def show_info(self):
        print(f"School: {self.number}")

class Subject:
    def __init__(self, name, number_of_hours):
        self.name = name
        self.number_of_hours = number_of_hours

        if not isinstance(number_of_hours, int) or number_of_hours <= 0:
            raise ValueError("Number of hours should be a positive integer.")

    def show_info(self):
        print(f"Subject Name: {self.name}\nNumber of Hours: {self.number_of_hours}")


try:
    teacher = Teacher("Evgeniy Burduk", "1994-01-02", "Mathematics")
    teacher.show_info()
except Exception as e:
    print(f"Error: {e}")

try:
    student = Student("Alex Werbitskiy", "1993-03-04", "Computer Science")
    student.show_info()
except Exception as e:
    print(f"Error: {e}")

try:
    academy = Academy("Example Academy", "City Center")
    academy.show_info()
except Exception as e:
    print(f"Error: {e}")

try:
    college = College("Tech College", "Izmail", "Engineering")
    college.show_info()
except Exception as e:
    print(f"Error: {e}")

try:
    school = School("High School", "Downtown", "123")
    school.show_info()
except Exception as e:
    print(f"Error: {e}")

try:
    subject = Subject("Physics", 92)
    subject.show_info()
except Exception as e:
    print(f"Error: {e}")
