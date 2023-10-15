import pandas as pd
import requests
from io import StringIO
import numpy as np 

# This code will import the dataset from csv file.

# URL of the CSV file.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2021-01-01'

# Send an HTTP GET request to download the file.
response = requests.get(url)


# The CSV file does'nt have a header so we will create a list header containing name of header.

header = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
        "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
        "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
        "peak-rpm","city-mpg","highway-mpg","price"]


# This code will download and store data in auto.csv file.
if response.status_code == 200:
    df = pd.read_csv(StringIO(response.text), names = header) # Assign the header names.
    df.to_csv('auto.csv', index=False)
    #print('Data downloaded and saved as auto.csv')
else:
    print('Failed to download data. Status code:', response.status_code)


# dealing with missing values.
df = pd.read_csv('auto.csv') 
df.replace("?", np.nan, inplace=True)  #Replace ? to NaN
df.to_csv('auto.csv', index=False)
print('? is replaced by NaN')  

# Use the isna() or isnull() function to create a Boolean mask for missing values.
missing_data = df.isnull()

#Count missing_data in each column.
for column in missing_data.columns.values.tolist():
    print (missing_data[column].value_counts())
    print("")   

# Calculate the mean value for the "normalized-losses", "bore", "stroke", "horsepower", "peak-rpm" column.
avg_norm_loses = df["normalized-losses"].astype("float").mean(axis=0)
avg_bore = df["bore"].astype("float").mean(axis=0)
avg_stroke = df["stroke"].astype("float").mean(axis=0)
avg_horsepower = df["horsepower"].astype("float").mean(axis=0)
avg_peakrpm = df["peak-rpm"].astype("float").mean(axis=0)

# Replace "NaN" with mean value in "normalized-losses", "bore", "stroke", "horsepower", "peak-rpm" column.
df["normalized-losses"].replace(np.nan, avg_norm_loses, inplace = True)
df["bore"].replace(np.nan, avg_bore, inplace=True)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)
df["horsepower"].replace(np.nan, avg_horsepower, inplace=True)
df["peak-rpm"].replace(np.nan, avg_peakrpm, inplace=True)

# print("Average of normalized-losses:",avg_norm_loses)
# print("Average of bore:",avg_bore)
# print("Average of stroke:",avg_stroke)
# print("Average of horsepower:",avg_horsepower)
# print("Average of peak-rpm:",avg_peakrpm)
#print(df.head(100))  

# Calculate the most occuring value in num-of-doors column.
most_num_doors = df["num-of-doors"].value_counts().idxmax()

# Replace "NaN" with most frequent value in "num-of-doors" column.
df["num-of-doors"].replace(np.nan, most_num_doors, inplace=True)

# Finally, let's drop all rows that do not have price data:
# Simply drop whole row with Nan in "price" column.
df.dropna(subset=["price"], axis=0, inplace=True)

# Reset index, because we dropped two rows.
df.reset_index(drop=True, inplace=True)

# Now you can count missing values using the method used earlier and there will be none.


# Let's list the datatypes for each columns.
print(df.dtypes)

# Convert data types to proper format.
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

# Now we have finally obtained the cleaned dataset with no missing values with all data in its proper format.
# Let us list the datatypes after conversion.
print(df.dtypes)

## We will normalize the length, width and height column.
df["length"] = df["length"]/df["length"].max()
df["width"] = df["width"]/df["width"].max()
df["height"] = df["height"]/df["height"].max()

# Finally make a new csv file named ' auto-clean' using to_csv function.
df.to_csv('auto_clean.csv', index=False)
