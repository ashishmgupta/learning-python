import pandas as pd

# Creating a dataframe
# A dataframe is a collection of serieses.
# In the below example, c1 and c2 are serieses with values 1,2,3 and 4,5,6 in them respectively
df = pd.DataFrame({"c1":[1,2,3], "c2":[4,5,6]})
print(df)

# Get the row where column C1 has value 2
df1 = df[df["c1"] == 2]
print(df1)

# Get the row which has max value of c2
df2 = df[df["c2"] == df["c2"].max()]
print(df2)


# Call a function on each value for a specific column of the dataframe
def increment(x):
    return str(x)+"_"+str(x+2)

result = [increment(x) for x in df["c1"]]
print(result)
print(type(result))

# Iterating through the rows of a dataframe
for i, row in df.iterrows():
    print(str(row["c1"]) + "--" + str(row["c2"]))
