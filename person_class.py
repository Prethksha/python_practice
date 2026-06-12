class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def __repr__(self):
        return f"Roll: {self.roll_no} | Name: {self.name} | Age: {self.age}"
    
class person:
    def __init__(self,name, age):
        self.name= name
        self.age=age

class student(person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no= roll_no

    def __repr__(self):
        return f"Roll: {self.roll_no} | Name: {self.name}  | Age: {self.age}"
    