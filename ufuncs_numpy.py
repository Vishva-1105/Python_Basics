x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i,j in zip(x, y):
    z.append(i+j)
print(z)

import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)

import numpy as np
def myadd(x, y):
    return x + y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

import numpy as np
print(type(np.add))

import numpy as np
print(type(np.concatenate))

if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')

#absolute value
import numpy as np
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)

#truncation
import numpy as np
arr = np.trunc([-3.1666, 3.6667])
print(arr)
#or
arr = np.fix([-3.1666, 3.6667])
print(arr)

#Rounding
import numpy as np
arr = np.around(3.166, 2)
print(arr)

#Floor
import numpy as np
arr = np.floor([-3.1666, 3.6667])
print(arr)

#ceil
import numpy as np
arr = np.ceil([-3.1666, 3.6667])
print(arr)

#python JSON module
import json
data = {"name": "Alice", "age": 22}
json_string = json.dumps(data)
print(json_string)

python_data = json.loads(json_string)
print(python_data["name"])

import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [22, 25, 30],
    "city" : ["Paris", "New york", "London"]
}
df = pd.DataFrame(data)
print(df)
print(df["Age"].mean())
print(df.describe())
