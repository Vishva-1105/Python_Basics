import pandas as pd
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings' : [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

print(pd.__version__)

print("\n")

a = [1, 7, 2]
myvar1 = pd.Series(a)
print(myvar1)
print(myvar1[0])
print("\n")

b = [4, 6, 8]
myvar2 = pd.Series(b, index = ["x", "y", "z"])
print(myvar2)
print(myvar2["y"])
print("\n")

calories = {"day1":420, "day2": 380, "day3": 390}
cal = pd.Series(calories, index = ["day1", "day2"])
print(cal)
print("\n")

data = {
    "calaries": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[[0,1]])
print("\n")

data1 = {
    "calories" : [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data1, index = ["day1", "day2", "day3"])
print(df)
print("\n", df.loc["day2"])

df_csv = pd.read_csv('data.csv')
print(df_csv.to_string())
print(pd.options.display.max_rows)
print("\n")

import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
print(df.tail())

print(df.info())

data_list = {
    "Duration": {
        "0":60,
        "1":60,
        "2":60,
        "3":45,
        "4":45,
        "5":60
    },
    "Pluse":{
        "0":117,
        "1":110,
        "2":117,
        "3":103,
        "4":109,
        "5":102
    },
    "Maxpulse":{
        "0":130,
        "1":145,
        "2":135,
        "3":175,
        "4":148,
        "5":127
    },
    "Calories":{
        "0":409,
        "1":479,
        "2":340,
        "3":282,
        "4":406,
        "5":300
    }
}
df = pd.DataFrame(data_list)
print(df)

new_df = df_csv.dropna()
print(new_df.to_string())

df_csv.dropna(inplace = True)
print(df_csv.to_string())

df_csv.fillna(130,inplace = True)

import pandas as pd
df = pd.read_csv('data.csv')
x = df_csv["Calories"].mean()
df_csv.fillna({"Calories": x}, inplace = True)

import pandas as pd
df = pd.read_csv('data.csv')
y = df_csv["Calories"].median()
df_csv.fillna({"Calories": y}, inplace = True)

import pandas as pd
df = pd.read_csv('data.csv')
z = df_csv["Calories"].mode()[0]
df_csv.fillna({"Calories": z}, inplace = True)

import pandas as pd
df1 = pd.read_csv('data.csv')
df1['Date'] = pd.to_datetime(df1['Date'], format='mixed')
print(df1.to_string())

import pandas as pd
df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'], format = 'mixed')
df.dropna(subset = ['Date'], inplace = True)
df.loc[7, 'Duration'] = 45
for x in df.index:
    if df.loc[x, "Duration"]> 120:
        df.loc[x, "Duration"] = 120
print(df.to_string())


df.drop_duplicates(inplace = True)
print(df.to_string())
print(df.corr())

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()




import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df["Duration"].plot(kind='hist')

plt.show()

