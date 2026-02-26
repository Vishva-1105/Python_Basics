import numpy


class Cat:
    def sound(self):
        print("Meow")


class Dog:
    def sound(self):
        print("Bark")


for animal in (Cat(), Dog()):
    animal.sound()
print("--------------------------------\n")


class Employee:
    company = "TechM"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {Employee.company}")

    def increment(self, amount):
        self.salary += amount

emp1 = Employee("Rahul", 5000)
emp1.increment(5000)
emp1.show_details()

class BankAccount:
    bank_name = "National Bank"
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance +=amount
            print(f"{amount} deposited amount.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")

    def get_balance(self):
        return self.__balance

    def display_account(self):
        print("-----Account Details-----")
        print("Bank:", BankAccount.bank_name)
        print("Account Holder:", self.account_holder)
        print("Balance", self.__balance)
        print("-------------------------")


acc1 = BankAccount("Rahul", 1000)
acc2 = BankAccount("Anita", 5000)

acc1.deposit(500)
acc1.withdraw(300)
acc1.display_account()

acc2.withdraw(6000)
acc2.display_account()


class InvalidAgeError(Exception):
    pass
age = int(input("Enter age: "))

if age < 18:
    raise InvalidAgeError("Age must be 18+")
print("--------------------------------\n")

# __init__ method
class Home:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Home("Email")
p2 = Home("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)
print("--------------------------------\n")

# self Parameter
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

Vehicle1 = Vehicle("Toyota", "Corolla", 2020)
Vehicle1.display_info()

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

p1 = Employee("Tobias", 25, 50000)
print(p1.age)

p1.age = 26
print(p1.age)
print("--------------------------------\n")

#Class property vs instance property
class Person:
    species = "Human"
    def __init__(self, name):
        self.name = name

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
print("--------------------------------\n")

# Add new properties
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Tobias")
p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)
print("--------------------------------\n")

#class Methods
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Email")
p1.greet()
print("--------------------------------\n")

# class method with parameter
class Calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5,3))
print(calc.multiply(4,7))
print("--------------------------------\n")

#Method Accessing Properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())
print("--------------------------------\n")

#methods modifying Properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birhday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()
print("--------------------------------\n")

# __str__() Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)
print("--------------------------------\n")

#Multiple Methods
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

class Dog:
    def __init__(self, name, breed="Mixed", age=1):
        self.name = name
        self.breed = breed
        self.age = age

d1 = Dog("Buddy")
d2 = Dog("Max", "Golden Retriever")
print(d1.name, d1.breed, d1.age)
print(d2.name,d2.breed, d2.age)

class Teacher:
    def __init__(self, *args):
        if len(args) == 1 & isinstance(args[0], str):
            self.name = args[0]

        elif len(args) ==2:
            self.name = args[0]
            self.sub = args[1]

        elif isinstance(args[0], int):
            self.strength = args[0]

t1 = Teacher("Preeti Srivastav")
print('Name of the teacher is ',t1.name)

t2 = Teacher("Preeti Srivastav", "Computer science")
print(t2.name, ' teacher', t2.sub)

t3 = Teacher(32)
print("Strength of the class is", t3.strength)
print("--------------------------------\n")

#Inheritance
class Person1:
    def __init__(self, f_name, l_name):
        self.firstname = f_name
        self.lastname = l_name

    def printname(self):
        print(self.firstname, self.lastname)

x = Person1("John", "Doe")
x.printname()

class Student(Person1):
    def __init__(self, f_name, l_name, year):
        super().__init__(f_name, l_name)
        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)

x = Student("Mike", "Olsen", 2020)
x.printname()
print("--------------------------------\n")

#Polymorphism
#string
x = "Hello World!"
print(len(x))

#Tuple
my_tuple = ("apple","banana","cherry")
print(len(my_tuple))

#Dictionary
this_dict ={
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(len(this_dict))
print("--------------------------------\n")

#inheritance class polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Sail!")
class Plane(Vehicle):
    def move(self):
        print("FLy!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

print("--------------------------------\n")

#Encapsulation (Private Properties)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(22)
print(p1.get_age())

print("--------------------------------\n")

#encapsulation for protect and validate data
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):
        return self.__grade

    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"

student = Student("Emily")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())
print("--------------------------------\n")

#protected properties in encapsulation
class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) #can access, but shouldn't
print("--------------------------------\n")

#private Methods in encapsulation
class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        if not isinstance(num, (int, float)):
            return False
        return True

    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
print("--------------------------------\n")

#Nmae Mangling
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p1 = Person("Emily", 30)
print("age: ", p1._Person__age)
print("--------------------------------\n")

#accessing inner class from outside:
class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()
print("--------------------------------\n")

#accessing Outer class from Inner class
class Outer:
    def __init__(self):
        self.name = "Emily"

    class Inner:
        def __init__(self, outer):
            self.outer = outer
        def display(self):
            print("Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()
print("--------------------------------\n")

#example of inner class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "Off"
        def start(self):
            self.status = "Running"
            print("Engine started")
        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()
print("--------------------------------\n")

#Multiple inner classes
class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:
        def process(self):
            print("Processing data...")

    class RAM:
        def store(self):
            print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()

print("--------------------------------\n")
# all concepts
class PayrollSystem:
    def __init__(self, employees):
        print("Calculating Payroll")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f" - Check amount: {employee.calculate_payroll()}")
            print("")

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

class Order:
    def __init__(self, customer, product, quantity, price):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.price = price

    def total_amount(self):
        return self.quantity * self.price

o1 = Order("Riya", "Laptop", 1, 50000)
print("Total:", o1.total_amount())

print("--------------------------------\n")

import datetime
d= datetime.date(2025, 2, 12)
now = datetime.datetime.now()
print(d)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print("\n")

import pandas as pd
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())





