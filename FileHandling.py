file = open("data.txt", "r")

with open("data.txt", "r") as f:
    content = f.read()
    print(content)

with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)

with open("data.txt", "w") as f:
    f.write("New Data")

with open("data.txt", "a") as f:
    f.write("\nHello")

import csv
with open("data.csv", "r") as f:
    reader= csv.reader(f)
    for row in reader:
        print(row)

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])

try:
    print("Enter any number: ")
    num = int(input())
    print(10 / num)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done!")

print("\n")

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
finally:
    print("The 'try except' is finished!")

print("\n")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
print("\n")

import csv
try:
    with open("students.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["Name"], row["Age"])
except FileNotFoundError:
    print("File does not exist.")
except KeyError:
    print("Column missing in  CSV.")
finally:
    print("Program finished.")

import math
class Solver:
    def demo(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            return root1, root2
        elif d == 0:
            return -b / (2 * a)
        else:
            return "This equation has no roots"

if __name__ == '__main__':
    solver = Solver()

    while True:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        result = solver.demo(a,b,c)
        print(result)

