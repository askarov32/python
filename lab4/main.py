import pandas as pd
import numpy as np

# 1) Load auto-mpg.data into a DataFrame autodf.
column_names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']

autodf = pd.read_csv('auto-mpg.data', sep='\s+', names=column_names, na_values='?')
print(autodf.head())

# 2) Give description of the generated DataFrame autodf. (Description-> Main Statistics) .describe() OR aggregate()
autodf.describe()

# 3) Display the first 10 rows of the DataFrame autodf.  head(10)
print(autodf.head(10))

# Find the attributes which have missing values.
# Handle the missing values using following two
# ways:
   
#    i. Replace the missing values by a value before
# that. method = 'pad'
autodf.ffill(inplace=True)

# ii. Remove the rows having missing values from
# the original dataset
#             dropna()
autodf.dropna(inplace=True)

# 5) Print the details of the car which gave the maximum mileage.
max_mileage_car = autodf.loc[autodf['mpg'].idxmax()]
print(max_mileage_car)

# 6) Find the average displacement of the car given the number of cylinders.
autodf.groupby('cylinders')['displacement'].mean()

# 7) What is the average number of cylinders in a car? [cylinder] -> mean
autodf['cylinders'].mean()

# 8) Determine the no. of cars with weight greater than the average weight.

avg_weight = autodf['weight'].mean()
num_cars_above_avg_weight = autodf[autodf['weight'] > avg_weight].shape[0]
print(num_cars_above_avg_weight)

auto_min_hp = autodf.loc[autodf['horsepower'].idxmin()]

print("минимальное значение лошадиных сил", auto_min_hp)
