print(" \"Python Fundamentals\" " )
print("-Variables and Data types")
x = 5
y = "John"
z=True
print("x is" ,x)
print("y is" ,y)
print("Data type of variable x", type(x))
print("Data type of variable y", type(y))
print("Data type of variable z", type(z), "\n")

a = str(3)
b = int(3)
c = float(3)
d = bool(3>2)
print("this is string:" ,a)
print("this is integer:" ,b)
print("this is float:" ,c)
print("this is boolean:" ,d,"\n")

print("-Global Variable")
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x + "\n")
print("-Input & Output")
age = input("Enter your age: ")

if int(age) >= 18:
    print ("You are eligible to vote","\n")
else:
    print("You are not older enough to vote","\n")

print("-Type Casting")
print("string to integer")
age = input("Enter your age: ")
age = int(age)

print("Your age after adding 5 years:" , age + 5,"\n")

print("-Basic Arithmetic operations")
a = input("Enter any integer number a: ")
b = input("Enter any integer number b: ")
a = int(a)
b = int(b)

print("Addition of a and b:", a + b)
print("Division of a and b:", a / b)
print("Modulus of a and b:", a % b)
print("Multiplication of a and b:", a * b)
print("a raise to power b:", a ** b,"\n")

print("----Mini Project by using this topics----")
print("-students marks calculater")

name = input("Enter student name: ")

math = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

total = math + science + english
average = total / 3

print("\n--- Result ---")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 40:
    print("Status: PASS")
    print("Congratulations! \n")
else:
    print("Status: FAIL")
    print("You need to improve your skills \n")

print("---python Dictionary example---")

car={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x=car.keys()
print(x)
car ["color"] = "black"
print(x)
car ["Price"] = "1 cr"
print(x)

dictValue=car.values()
print(dictValue)

dictItem=car.items()
print(dictItem)

car["year"]=2020
print(car)
if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary \n")
else:
    print("No, 'model' is not one of the keys in the car dictionary \n")

print("print all the elements in the different line")
for x in car:
    print(x)
print("\nprint all the values in the different line")
for x in car:
    print(car[x])

print("\nprint all the elements and values in the separate line")
for x,y in car.items():
    print(x , y)