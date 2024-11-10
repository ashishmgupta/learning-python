import pandas as pd

# Reading from CSV
df = pd.read_csv(file_path)
print(df)
print(df["day"])

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


# url.csv
#id,api_url
#1,https://checkip.amazonaws.com
#2,https://checkip.amazonaws.com
#3,https://checkip.amazonaws.com
#4,https://checkip.amazonaws.com

# Add a column in the abobe file with status code of the response on call of each API in each row
import requests
import pandas as pd
def getStatusForUrl(url):
    resp = requests.get(url)
    return resp.status_code


df_api = pd.read_csv("url.csv")
df_api["status"] = [getStatusForUrl(x) for x in df_api["api_url"]]
#id,api_url,status
#1,https://checkip.amazonaws.com,200
#2,https://checkip.amazonaws.com,200
#3,https://checkip.amazonaws.com,200
#4,https://checkip.amazonaws.com,200
