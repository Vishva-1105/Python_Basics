
def print_hi(name):

    print(f'Hello, {name}!')

if __name__ == '__main__':
    print_hi('PyCharm')
print("____________________")

for i in range(0, 10, 2):
    print(i)
print("____________________")
count = 0
while (count<3):
    count = count + 1
    print("heii!!")
print("____________________")
n = 42
f = 3.14
s = "Hello, Everyone!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

print(type(n))
print(type(f))
print(type(s))
print(type(li))
print(type(d))
print(type(bool))
print("____________________")
name = "Alex"
age = 1

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome Back.")
else:
    print("Good Bye!!")

print("____________________")

print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)

print("____________________")
a = 15
b = 4

print("Addition:", a + b)

print("Subtraction:", a - b)

print("Multiplication:", a * b)

print("Division:", a / b)

print("Floor Division:", a // b)

print("Modulus:", a % b)

print("Exponentiation:", a ** b)

print("____________________")
p = 13
q = 33

print(p > q)
print(p < q)
print(p == q)
print(p != q)
print(p >= q)
print(p <= q)
print("____________________")

s = ["Home", "Sweet", "Home"]
print("Accessing element from the list")
print(s[0])
print(s[2])

print("Accessing element using negative indexing")
print(s[-1])
print(s[-2])
print("____________________")

for letter in 'lifeupdate':
    if letter == 'e' or letter == 'f':
        break

print('Current Letter :', letter)
print("____________________")

for letter in 'Helloguys':
    pass
print('Last Letter :', letter)
print("____________________")

def evenOdd(x):
    if (x % 2) == 0:
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))

print("____________________")
fruits=("apple","banana","mango")
new_fruits=list(fruits)
new_fruits[1]="pineapple"
c=tuple(new_fruits)
print(c)
print("____________________")


x=frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
print("____________________")

set1={"a","b","c"}
set2={1,2,3,4}
set3={"Jhon","Alex","Alina"}
set4={"apple","banana","cherry"}
total=set1.union(set2,set3,set4)
print(total)
myset = set1 | set2 | set3 |set4
print(myset)
print("____________________")

child1={
    "name" : "Emil",
    "year" : 2004
}
child2={
    "name" : "Tobias",
    "year" : 2007
}
child3={
    "name" : "Alina",
    "year" : 2011
}
child4={
    "name" : "Alex",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3,
    "child4" : child4
}
print("name of child2:",myfamily["child2"]["name"])
print("born year of child4:",myfamily["child3"]["year"])

a=400
b=54
c=640
if a>b and c>a:
    print("\nBoth conditions are True")
elif a>b or c>a:
    print("\nAny one comdition is True")

print("\n")
for x in range(18):
    print(x)
else:
    print("End")

def the_function(person):
    print("Name:",person['name'])
    print("Age:",person['age'])

def my_function():
    print("Hello from a function")

my_function()
my_function()
my_function()
print("\n")

a=[10,20,30,40,50]
a.remove(30)
print("After remove(30):",a)

popped_val = a.pop(1)
print("Popped element:", popped_val)
print("After pop(1):",a)

del a[0]
print("After del a[0]:",a,"\n")

a=['apple','banana','cherry']
for item in a:
    print(item)

print("\n")
matrix=[ [1,2,3],
         [4,5,6],
         [7,8,9]]
print(matrix[1][2])

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9
print("value in celcius:",fahrenheit_to_celcius(45))
print("value in celcius:",fahrenheit_to_celcius(77))
print("value in celcius:",fahrenheit_to_celcius(50),"\n")

tup=(5,'welcome',7,'User')
print(tup)

tup1=(0,1,2,3)
tup2=('python','lerner')
tup3=(tup1,tup2)
print(tup3)
tup1=('Hi',)*3
print (tup1)
tup=('Hi')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup,"\n")

tup = tuple("hello")
print(tup[0])
print(tup[1:4])
print(tup[:3])

tup = ("To","Do","List")
a,b,c=tup
print(a)
print(b)
print(c ,"\n")

test_list = [(None,2),(None,None),(3,4),(12,3),(None, )]
print("The original list is:" +str(test_list))
res = list(filter(lambda sub : not all(ele == None for ele in sub),test_list))
print("Removed None Tuples : " + str(res),"\n")

test_list = [(None, None),(None, None),(3,4),(12,3),(None, )]
def r_tuple(lst,res):
    if not lst:
        return res
    elif None in lst[0]:
        return r_tuple(lst[1:],res)
    else:
        res.append(lst[0])
        return r_tuple(lst[1:],res)
new_list = r_tuple(test_list,[])
print("Remove None Tuples:"+ str(new_list))
print("\n")

s="Python"
for char in s:
    print(char)
print("\n")

def my_function():
    return ["apple","banana","cherry","grapes"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3] ,"\n")

def v_function(*numbers):
    if len(numbers)==0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num=num
    return max_num
print(v_function(3,7,2,9,1))

def k_function(username, **details):
    print("\nUsername:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)
k_function("email123",age= 25, city= "Oslo",hobby="coding")

print("\n")
def a_function(contry = "Norway"):
    print("I am from", contry)

a_function("Sweden")
a_function("India")
a_function()
a_function("Brazil")
print("\n")
def ani_function(animal, name):
    print("I have a", animal)
    print("my", animal + "'s name is", name)

ani_function(name = "Buddy", animal = "dog")

print("\n")
def my_function(greeting,*names):
    for name in names:
        print(greeting, name)
my_function("Hello","Emil","Tobias","Linus")

print("\n")
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5) , "\n")

def my_function(fname, lname):
    print("Hello", fname, lname)

person={"fname":"Emil","lname":"Refsnes"}
my_function(**person)

print("\n")
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

def myfunc(n):
    return lambda a: a* n
mytripler = myfunc(3)
mydoubler = myfunc(2)
print(mytripler(11))
print(mydoubler(11))

print("\n")
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

print("\n")
def countdown(n):
    if n<= 0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)

countdown(3)
print("\n")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
print("\n")


def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))
print("\n")

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

my_list = [1,2,3,4,5]
print(sum_list(my_list))
print("\n")

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)
print("\n")

def large_sequence(n):
    for i in range(n):
        yield i

gen = large_sequence(100000)
print(next(gen))
print(next(gen))
print(next(gen))
print("\n")

list_comp = [x * x for x in range(5)]
print(list_comp)

gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))
print("\n")

def echo_generator():
    while True:
        received = yield
        print("Received: ", received)

gen = echo_generator()
next(gen)
gen.send("Hello")
gen.send("From")
gen.send("Vishva")
print("\n")

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")

gen= my_gen()
print(next(gen))
gen.close()

print("\n")
mytuple = ("apple", "banana", "cherry")
myit= iter(mytuple)
print(next(myit))
print(next(myit))
print("\n")

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("\n")
class MyNumbers:
    def __iter__(self):
        self.a= 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
print("\n")

import mymodule as mx

a=mx.person1["age"]
print(a)

import platform
x = platform.system()
print(x)
y = dir(platform)
print(y)

from mymodule import person1
print (person1["age"])
print("\n")

import datetime
z = datetime.datetime.now()
print("year,month,day,hour,minute,sec and microsec:",z)
print("Year:",z.year)
print("Weekday:",z.strftime("%A"))
print("Century:",z.strftime("%C"))

x = datetime.datetime(2020, 5, 17)
print(x)
print("\n")

import json
x = '{"name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print("age:", y["age"])
print("\n")

import json
x = {
    "name": "jhon",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x, indent=3, sort_keys=True))
print("\n")

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("YES! We have a match!")
else:
    print("No match")
print("\n")

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)
print("\n")

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)
print("\n")

price = 59000
txt = f"The price is {price:,} dollers"
print(txt)
print("\n")

price = 49
txt = "The price is {} dollars"
print(txt.format(price))
print("\n")

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollers."
print(myorder.format(quantity, itemno, price))
print("\n")

print("Enter your name here:")
name = input()
print(f"Hello {name}, Nice to meet you!")
print("\n")

y= True
while y == True:
    x = input("Enter a number:")
    try:
        x = float(x)
        y = False
    except:
        print("Wrong in put,  Please try again.")

print("Thank you!")
print("\n")

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
p1 = Person("Emil", 36)
p2 = Person("Alise")

print(p1.name, p1.age)
print(p2.name, p2.age)
print("\n")

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person2("Email", 25)
p1.greet()
print("\n")

class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person3("Tobias", 25)
print("age:",p1.age)

p1.age = 26
print("age:",p1.age)
print("\n")


class Human:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

h1 = Human("Tobias", 23)
print("age: ",h1.get_age())
print("\n")

