from importlib.metadata import distribution

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))
print("\n")

arr1 = np.array((1, 2, 3, 4, 5))
print(arr1)

print("the given array is :", arr1)
print("\n")

#0-D Array
import numpy as np
arr2 = np.array(42)
print("0-D Array is: ",arr2)
print("\n")

#1-D Array
arr3 = np.array([1, 2, 3, 4, 5])
print("1-D Array is: \n",arr3)

#2-D Array
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D Array is: \n",arr4)

#3-D Array
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("3-D Array is: \n",arr5)
print("\n")

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print("dimension of array a: ",a.ndim)
print("dimension of array b: ",b.ndim)
print("dimension of array c: ",c.ndim)
print("dimension of array d: ",d.ndim)
print("\n")

arr = np.array([1, 2, 3, 4], ndmin=5)
print("5 dimensional array: ",arr)
print('number of dimensions :', arr.ndim)
print("\n")

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("from index-1 to index-5: ",arr[1:5])
print("from index-4 to the end: ",arr[4:])
print("from the beginning to index-3: ",arr[:4])
print("from index-3 from the end to index-1 from the end: ",arr[-3:-1])
print("\n")

#data type of an array
a = np.array([1.1, 2.1, 3.1])
newarr = a.astype('i')
print(newarr)
print(newarr.dtype)
print("\n")

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)
print("\n")

arr = np.array([1, 0, 3])
new = arr.astype(bool)
print(new)
print(new.dtype)
print("\n")

#copy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
print("\n")

#shape of array
arr = np.array([[1, 2, 3,4], [5, 6, 7, 8]])
print("shape of array :", arr.shape)

arr1 = np.array([1, 2, 3, 4], ndmin = 5)
print(arr1)
print("shape of array: ", arr1.shape)
print("\n")

#Reshaping
#from 1-D to 2-D
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print("Reshaping: \n",newarr)
print("\n")

#unknown dimension
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr1.reshape(2, 2, -1)
print(newarr)

#flattering the array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print("flattering of array: ",newarr)

#iteration
#iterating 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print("iteration of 2-D array: \n",x)

#iteration of each scalar element
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("iteration of each scalar element:")
for x in arr:
    for y in x:
        print( y)

#iteration of 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("iteration of 3-D array:")
for x in arr:
    print(x)

print("iteration of each scalar element:")
for p in arr:
    for q in p:
        for r in q:
            print(r)
print("\n")

import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)

print("\n")
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

print("\n")

#iterating with different step size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("different step size iteration")
for x in np.nditer(arr[:, ::2]):
    print(x)

#enumerated iteration
#Enumerate 2-D array
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
print("\n")

#join two arrays
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print("join two arrays :",arr)
print("\n")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6],[7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
print("\n")

#stacking along Rows
print("stacking along Rows:")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)
print("\n")

#stacking along Columns
print("stacking along column:")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)
print("\n")

#stacking along height
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print("stacking along height: \n",arr)

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print("split the array in 4 parts: \n",newarr)
print("\n")

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

#splitting 2-D Arrays
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8],[9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
print("\n")

#using package:
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

#random numbers
#generate random number
from numpy import random
x = random.randint(100)
print(x)
 #generate random float
y = random.rand()
print(y)

#generate random Array
#for 1-D array
z = random.randint(100, size=(5))
print(x)

#for 2-D array
x = random.randint(100, size = (3, 5))
print(x)

#random number using choice()
from numpy import random
x = random.choice([3, 5, 7, 9])
print(x)

y = random.choice([3, 5, 7, 9], p= [0.1, 0.3, 0.6, 0.0], size= (100))
print(y)

#shuffle
from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

import matplotlib.pyplot as plt
import seaborn as sns
sns.displot([0, 1, 2, 3, 4, 5])
plt.show()

x = random.normal(loc = 1, scale = 2, size =(2, 3))
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde")

plt.show()

sns.displot(random.binomial(n=10, p=0.5, size=1000))
plt.show()

data = {
    "normal":random.normal(loc=50, scale=5, size=1000),
    "Binomial":random.binomial(n=100, p=0.5, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

#poisson distribution
x = random.poisson(lam=2, size=10)
print(x)

#visualization of poisson distribution
sns.displot(random.poisson(lam=2, size=1000 ))
plt.show()

#difference between normal and poisson distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "normal": random.normal(loc=50, scale=7, size=1000),
    "poisson": random.poisson(lam=50, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

#difference between binomial and poisson distribution
data ={
    "binomial": random.binomial(n=1000, p=0.01, size=1000),
    "poisson": random.poisson(lam=10, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

#uniform distribution
from numpy import random
x = random.uniform(size=(2, 3))
print(x)

#visualization of uniform distribution
from numpy import random
import matplotlib.pyplot as plt

sns.displot(random.uniform(size=1000), kind="kde")
plt.show()

#logistic distribution
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

#visualization of logistic distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.logistic(size=1000), kind="kde")
plt.show()

#difference between logistic and normal distribution
data= {
    "normal": random.normal(scale=2, size=1000),
    "logistic": random.logistic(size=1000)
}
sns.displot(data, kind="kde")
plt.show()

#multinomial Distribution(n, pvals)
from numpy import random
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)

#exponential distribution
y = random.multinomial(scale=2, size=(2,3))
print(y)

#visualization of exponential distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.exponential(size=1000), kind="kde")
plt.show()

#chi square distribution(df, size)
from numpy import random
x = random.chisqare(df=2, size=(2, 3))
print(x)

#visualization of chi square distribution
sns.displot(random.chisquare(df=2,size=1000), kind="kde")
plt.show()

#Rayleigh distribution(scale, size)
from numpy import random
x = random.rayleigh(scale=2, size=(2, 3))
print(x)

#visualization of rayleigh distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.rayleight(size=1000), kind="kde")
plt.show()

#pareto distribution(a, size)
from numpy import random
x = random.pareto(a=2, size=(2, 3))
print(x)

#visualization of pareto distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.pareto(a=2, size=1000))

plt.show()

#zipf distribution(a, size)
from numpy import random
x = random.zipf(a=2, size=(2, 3))
print(x)

#Visualization of Zipf distribution
import matplotlib.pyplot as plt
import seaborn as sns
x = random.zipf(a=2, size=1000)
sns.displot(x[x<10])
plt.show()

