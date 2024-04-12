

import pandas as pd
df = pd.DataFrame({'numbers' : [1,2,3] , 'colors' : ['red' , 'white' , 'blue'] } , columns = ['numbers' , 'colors'])
print(df)

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(5,3) , columns = ['N1' , 'N2' , 'N3'])
print(df)

import pandas as pd
df = pd.DataFrame({'N1' : [1,2,3,4] , 'N2' : [4,3,2,1]})
print(df)

import pandas as pd
L = [{'Name' : 'John' , 'Last Name' : 'Smith'},
      {'Name' : 'Mary' , 'Last Name' : 'Wood'}]
df = pd.DataFrame(L)
print(df)

import pandas as pd
data = np.loadtxt("sample.txt" , delimiter = ',')
print(data)

data = pd.read_csv("sample.txt", delimiter = ',')
print(data)
print("Print column Score")
print(data.Score)

df = pd.DataFrame(np.random.randn(10,3), columns=['N1' , 'N2' , 'N3'])
print(df)








#ex1
import pandas as pd


# Read the CSV file into a DataFrame
data = pd.read_csv("iris.csv", delimiter=',')
print(data.head(5))
# Function to compute mean
def mean(column):
    return sum(column) / len(column)

# Function to compute standard deviation
def std_dev(column, mean_value):
    squared_diff = [(x - mean_value) ** 2 for x in column]
    variance = sum(squared_diff) / len(column)
    return variance ** 0.5

# Function to compute min and max
def min_max(column):
    return min(column), max(column)



# Compute statistics
count = len(data)
mean_values = [mean(data[column]) for column in data.columns[:-1]]  # Exclude the last column (assuming it's the target variable)
std_values = [std_dev(data[column], mean(data[column])) for column in data.columns[:-1]]
min_max_values = [min_max(data[column]) for column in data.columns[:-1]]

# Create a DataFrame to show the results
result_data = {
    'Statistic': ['Count', 'Mean', 'Std Dev', 'Min', 'Max'],
    'SepalLength': [count] + mean_values[:1] + std_values[:1] + list(min_max_values[0]),
    'SepalWidth': [count] + mean_values[1:2] + std_values[1:2] + list(min_max_values[1]),
    'PetalLength': [count] + mean_values[2:3] + std_values[2:3] + list(min_max_values[2]),
    'PetalWidth': [count] + mean_values[3:4] + std_values[3:4] + list(min_max_values[3])
}

result_df = pd.DataFrame(result_data)
print(result_df)








#ex2
import pandas as pd

def calculate_mean(column):
    return sum(column) / len(column)

def calculate_std_dev(column, mean):
    squared_diff = [(x - mean)**2 for x in column]
    variance = sum(squared_diff) / len(column)
    return variance**0.5

def calculate_min_max(column):
    return min(column), max(column)

data = pd.read_csv('population.csv')
print(data.head())

# Group by Year and Country
data_by_year_country = data.groupby(['Year'])

results_df = pd.DataFrame(columns=['Year', 'Count', 'Mean', 'Std', 'Min', 'Max'])

for year, group in data_by_year_country:
    values = group['Value']

    count_value = len(values)
    mean_value = calculate_mean(values)
    std_value = calculate_std_dev(values, mean_value)
    min_value, max_value = calculate_min_max(values)

    # Add results to the dataframe
    if results_df.empty:
        results_df = pd.DataFrame([[year, count_value, mean_value, std_value, min_value, max_value]], columns=['Year', 'Count', 'Mean', 'Std', 'Min', 'Max'])
    else:
        results_df = pd.concat([results_df, pd.DataFrame([[year, count_value, mean_value, std_value, min_value, max_value]], columns=['Year', 'Count', 'Mean', 'Std', 'Min', 'Max'])])


results_df.reset_index(drop=True, inplace=True)

print(results_df)