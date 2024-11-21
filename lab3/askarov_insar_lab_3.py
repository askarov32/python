import numpy as np

# Exercise 1

nums = [1, 2, 23, 90, 12, 4, 7, 12, 20]
array = np.array(nums)

# a 
print("All numbers are divided by 2:", array / 2)

# b
myarray1 = np.array([-12, 23, 2, 4, 5, 94])
myarray2 = np.array([-13, 1, 22, 1, 45, 100])

# c
difference = myarray2 - myarray1
print(f"The difference between {myarray1} and {myarray2} is: ", difference)

# d
product = myarray1 * myarray2
print(f"The product of {myarray1} and {myarray2} is:", product)

# e
myarray1 = np.array([[1, 2], [3, 4]])  
myarray2 = np.array([[5, 6], [7, 8]])  

result = np.dot(myarray1, myarray2)  

print(f"The matrix multiplication of {myarray1} and {myarray2} is:", result)

# f
myarray1 = np.array([-12, 23, 2, 4, 5, 94])
myarray2 = np.array([-13, 1, 22, 1, 45, 100])

division = myarray1 / myarray2
print(f"The division of {myarray1} by {myarray2} is:", division)

# g
cubed_array_divided = (myarray1 ** 3) / 2
print("Cubed array was divided by 2:", cubed_array_divided)

# Exercise 2

myarray4 = np.arange(-1, -1 + (14 * 3 * 0.25), 0.25).reshape(14, 3)

print("myarray4:\n", myarray4)

splits = np.array_split(myarray4, 3)

for i, array in enumerate(splits):
    print(f"\nSplit {i + 1}:\n", array)
  
# a
print("The sum of all elements:", np.sum(myarray4))

# b
print("The sum of all elements row-wise:", np.sum(myarray4, axis=1))

# c
print("The sum of all elements column-wise:", np.sum(myarray4, axis=0))

# d
print("The max element:", np.max(myarray4))

# e
print("The min element:", np.min(myarray4))

# f
print("The mean of the elements:", np.mean(myarray4))

# g
print("The standard deviation column-wise:", np.std(myarray4, axis=0))

# exercise 3

print("\nexercise 3\n")

iris_data = np.genfromtxt('iris.txt', skip_header=1, delimiter=',', dtype=float)
irises = iris_data[:, :4] 

# 1. 
stats = {
    'max': np.around(np.max(irises, axis=0), 2),
    'min': np.around(np.min(irises, axis=0), 2),
    'mean': np.around(np.mean(irises, axis=0), 2),
    'std': np.around(np.std(irises, axis=0), 2),
    'var': np.around(np.var(irises, axis=0), 2)
}

for stat, values in stats.items():
    print(f"{stat.capitalize()} for columns: {values}")

# 2. 
iris_data_full = np.genfromtxt('iris.txt', skip_header=1, dtype='U', delimiter=',')

features = iris_data_full[:, :-1].astype(float) 
labels = iris_data_full[:, -1]  

def calculate_class_stats(class_data):
    return {
        'max': np.max(class_data, axis=0),
        'min': np.min(class_data, axis=0),
        'mean': np.mean(class_data, axis=0),
        'std': np.std(class_data, axis=0)
    }

iris_classes = {
    'Setosa': calculate_class_stats(features[labels == 'Setosa']),
    'Virginica': calculate_class_stats(features[labels == 'Virginica']),
    'Versicolor': calculate_class_stats(features[labels == 'Versicolor'])
}

for iris_class, class_stats in iris_classes.items():
    print(f"{iris_class} stats: {class_stats}")

# 3.
columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
min_values = [np.min(features[:, i]) for i in range(4)]  
print(f"Min values for {columns}: {min_values}")

comparison_results = {
    'Setosa': iris_classes['Setosa']['min'] > min_values,
    'Virginica': iris_classes['Virginica']['min'] > min_values,
    'Versicolor': iris_classes['Versicolor']['min'] > min_values
}

for iris_class, result in comparison_results.items():
    print(f"{iris_class} comparison with global minimum: {result}")
