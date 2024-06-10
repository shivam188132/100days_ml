import pandas as pd
data = {
    'X': ['a', 'b', 'c'],
    'Y': ['d', 'e', 'f'],
    'Z': ['g', 'h', 'i'],
    'W': ['j', 'k', 'l']
}
df = pd.DataFrame(data)
print(df)

m = df.iloc[:,1:2]
print(m)

n = df.iloc[1:,:]
print(n)