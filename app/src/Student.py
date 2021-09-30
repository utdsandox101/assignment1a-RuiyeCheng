# Create a class named Student
# The Student class must extend the Person class
# In addition to the Person class attribute, the Student class must have the following attributes:
#   1. id (int)
#   2. grade (float)
from app.src.Person import Person


class Student(Person):
    def __init__(self, name: str, age: int, id: int, grade: float):
        super().__init__(name, age)
        self.id = id
        self.grade = grade