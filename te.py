class Person:



    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print("Eating")

    def walk(self):
        print("Walking")

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

person = Person("Asiq", 30, "Male")
print("Name: " + person.name + " and age is " + str(person.age))

person2 = Person("Shuvo", 10, "Male")
print("Name: " + person2.name + " and age is " + str(person2.age))