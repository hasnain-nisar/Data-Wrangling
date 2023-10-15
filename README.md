# Data Wrangling

Data wrangling, also known as data munging, involves the process of gathering, selecting, and transforming raw data into a usable format for analysis.
It includes tasks like importing data from various sources, reshaping data, merging datasets, and aggregating information.
Data wrangling often starts with raw data and involves structuring and organizing it for further analysis.

This project is about cars data in which we want to predict the price of the cars. but before prediction or making any model the data must go through some data analysis or data cleaning process which are as below.

## Data Import & Storage.

Import a dataset from a CSV file hosted online and saves it as a local CSV file named "auto.csv." It uses the Pandas library to handle data and performs the following steps:

1. It sends an HTTP GET request to download the CSV file from the specified URL.
2. Since the CSV file doesn't have a header, a list of column names called "header" is defined to be assigned later.
3. If the HTTP request is successful (status code 200), the code reads the data into a Pandas DataFrame, assigns the header names, and saves it as "auto.csv."
4. A success message is displayed indicating that the data has been downloaded and saved.
5. If the request fails, an error message with the status code is displayed.

This code is useful for downloading datasets from the web, particularly when the data lacks a header. It provides a way to access and store the data locally for further analysis.

## Identify and Handle Missing values.

In the car dataset, missing data comes with the question mark "?". We replace "?" with NaN (Not a Number), Python's default missing value marker for reasons of computational speed and convenience. Here we use the function:
.replace(A, B, inplace = True)
to replace A by B.

## Evaluating for Missing Data

The missing values are converted by default. We use the following functions to identify these missing values. There are two methods to detect missing data:

.isnull()
.notnull()
The output is a boolean value indicating whether the value that is passed into the argument is in fact missing data."True" means the value is a missing value while "False" means the value is not a missing value.

We are evaluating the missing data in order to count missing values in each column.

## Count Missing values in each Column.

Using a for loop in Python, we can quickly figure out the number of missing values in each column. As mentioned above, "True" represents a missing value and "False" means the value is present in the dataset. In the body of the for loop the method ".value_counts()" counts the number of "True" values.

From the output we can see, each column has 205 rows of data and seven of the columns containing missing data:

1. "normalized-losses": 41 missing data
2. "num-of-doors": 2 missing data
3. "bore": 4 missing data
4. "stroke" : 4 missing data
5. "horsepower": 2 missing data
6. "peak-rpm": 2 missing data
7. "price": 4 missing data

## Deal with Missing Data.

This is an imp step. There are two methods to deal with missing data.

1. Drop data
   a. Drop the whole row.
   b. Drop the whole column.
2. Replace data
   a. Replace it by mean.
   b. Replace it by frequency.
   c. Replace it based on other functions.

Whole columns should be dropped only if most entries in the column are empty. In our dataset, none of the columns are empty enough to drop entirely. We have some freedom in choosing which method to replace data; however, some methods may seem more reasonable than others. We will apply each method to many different columns:

1. Replace by mean:

"normalized-losses": 41 missing data, replace them with mean
"stroke": 4 missing data, replace them with mean
"bore": 4 missing data, replace them with mean
"horsepower": 2 missing data, replace them with mean
"peak-rpm": 2 missing data, replace them with mean

2. Replace by frequency:

"num-of-doors": 2 missing data, replace them with "four".
Reason: 84% sedans is four doors. Since four doors is most frequent, it is most likely to occur

3. Drop the whole row:

"price": 4 missing data, simply delete the whole row
Reason: price is what we want to predict. Any data entry without price data cannot be used for prediction; therefore any row now without price data is not useful to us.

## Correct Data format.

The last step in data cleaning is checking and making sure that all data is in the correct format (int, float, text or other).

In Pandas, we use:

.dtype() to check the data type.
.astype() to change the data type.

As we can see in output, some columns are not of the correct data type. Numerical variables should have type 'float' or 'int', and variables with strings such as categories should have type 'object'. For example, 'bore' and 'stroke' variables are numerical values that describe the engines, so we should expect them to be of the type 'float' or 'int'; however, they are shown as type 'object'. We have to convert data types into a proper format for each column using the "astype()" method.

## Data Normalization

Why normalization?

Normalization is the process of transforming values of several variables into a similar range. Typical normalizations include scaling the variable so the variable average is 0, scaling the variable so the variance is 1, or scaling the variable so the variable values range from 0 to 1.

Example

To demonstrate normalization, let's say we want to scale the columns "length", "width" and "height".

Target: would like to normalize those variables so their value ranges from 0 to 1

Approach: replace original value by (original value)/(maximum value)

Now we have finally obtained the cleaned dataset with no missing values with all data in its proper format.
We saved this dataset in new CSV file named auto_csv.
