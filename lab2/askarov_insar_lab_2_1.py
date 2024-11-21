import numpy as np

# ASKAROV INSAR IT3-2208 LAB3
# 1. Given two fractions as tuples, multiply them.
# 2. Given two fractions as tuples, divide them.
# 3. Given a list of fractions as a tuple, return the one that is smallest in value.

def multiplication(fraction1, fraction2):
    numerator = fraction1[0] * fraction2[0]
    denominator = fraction1[1] * fraction2[1]
    return (numerator, denominator)

def division(fraction1, fraction2):
    numerator = fraction1[0] * fraction2[1]
    denominator = fraction1[1] * fraction2[0]
    return (numerator, denominator)

def smallest_fraction(fractions):
    smallest = min(fractions, key=lambda x: x[0] / x[1])
    return smallest

def show_fraction(fraction):
    return f"{fraction[0]}/{fraction[1]}"

print("Exercise 1:")

frac1 = input("Enter the fraction: ")
frac2 = input("Enter the fraction: ")

fraction1 = tuple(map(int, frac1.split("/")))
fraction2 = tuple(map(int, frac2.split("/")))

mult_result = multiplication(fraction1, fraction2)
div_result = division(fraction1, fraction2)
fraction_list = []

frac3 = input("Enter the fraction: ")
fraction_list.append(tuple(map(int, frac1.split("/"))))
while (frac3 != "stop"):
    fraction_list.append(tuple(map(int, frac3.split("/"))))
    frac3 = input("Enter the fraction: ")
    
smallest = smallest_fraction(fraction_list)

print(f"Multiplication of fractrions: {show_fraction(mult_result)}")
print(f"Division of fractions : {show_fraction(div_result)}")
print(f"The smallest fraction: {show_fraction(smallest)}")

# Take in numbers as input until “stop” is entered. Then split the numbers into three lists: one
# containing all the numbers, one containing all even values, and one containing all odd. Print
# out all three lists, as well as each list’s sum and average. Assume all input values are integers.

print("excercise 2: ")

numbers = []
even_numbers = []
odd_numbers = []

inp = input("Input a number: ")
while (inp != "stop"):
    int_input = int(inp)
    numbers.append(int_input)
    even_numbers.append(int_input) if int_input % 2 == 0 else odd_numbers.append(int_input)
    inp = input("Input a number: ")

def avg(array):
    np_arr = np.array(array)
    return np.average(np_arr)

print("All numbers: ", numbers)
print("Average of all numbers: ", avg(numbers))
print("Sum of all numbers: ", sum(numbers))
print("Even numbers: ", even_numbers)
print("Average of even numbers: ", avg(even_numbers))
print("Sum of even numbers: ", sum(even_numbers))
print("Odd numbers: ", odd_numbers)
print("Average of odd numbers: ", avg(odd_numbers))
print("Sum of odd numbers: ", sum(odd_numbers))

nums = numbers

# Take in numbers as input until “stop” is entered. As you take in each number, insert it into a list so that the list is sorted in ascending order. That is, look through the list until you find the place where the new element belongs, then use .insert() to place it there. If the number isalready in the list, do not add it again. After “stop” is entered, print out the list. Do not use
# any of Python’s built-in sorting functions.

print("excercise 3: ")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

numbers = []

inp = input("Input a number: ")
while (inp != "stop"):
    numbers.append(float(inp))
    print("List contains ", insertion_sort(numbers))
    inp = input("Input a number: ")

print(insertion_sort(numbers))

# Option 1

# Task 1

amount_pos = 0
for i in nums:
    if i > 0:
        amount_pos += 1

print(f"there are {amount_pos} positive numbers in {nums} list")

# Task 2

def getTheLargest(arr):
    max = min(arr)
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            index = i
    return max, index

max, index = getTheLargest(nums)
print(f"The largest number is {max} at index {index}")

if (odd_numbers):
    print(f"the smallest odd number is {min(odd_numbers)}")
else: 
    print(0)
    
    