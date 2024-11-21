# INSAR ASKAROV IT3-2208

import numpy as np

# 1.  Write a program to hold a small database of food items and their costs using two lists. 

print("excercise 1:")

food = ['eggs', 'beef', 'tomato', 'milk']
prices = [100, 200, 300, 400] # tenge

if len(food) != len(prices):
    print("The lengths of the food and prices lists do not match.")
else:
    for i in range(len(food)):
        try:
            print(food[i] + " costs " + str(prices[i]) + " tenge")
        except IndexError as ex:
            print("Index error:", ex)
        except Exception as ex:
            print("An error occurred:", ex)

# 2. Create a 2D array of zero integers, fill with some numbers and print out the full array then print out some slices from the array. 

print("\n")
print("excercise 2:")

array = np.zeros((3, 3))

array[0, :] = [0.5, 1.5, 2.5]
array[1, :] = [3.5, 4.5, 5.5]
array[2, :] = [6.5, 7.5, 8.5]

print("Full array:")
print(array)

print("\nSlice of the first two rows:")
print(array[:2, :])

print("\nSlice of the last two columns:")
print(array[:, 1:])

# 3. Create a list with the names of 10 'friends'. Create a second matching list with their years of birth.

print("\n")
print("excercise 3:")

friends = ['insar', 'alan', 'dias', 'dinara', 'timur', 'beibars', 'mark', 'bob', 'sam', 'kasym-zhomart']

years_of_birth = [2003, 2003, 2004, 2004, 2005, 2004, 2001, 1999, 1998, 1953]

if len(friends) != len(years_of_birth):
    print("The lengths of the freinds and years of birth lists do not match.")
else:
    for i in range(len(friends)):
        try:
            print(friends[i] + " is " + str(years_of_birth[i]) + " year of birth")
        except IndexError as ex:
            print("Index error:", ex)
        except Exception as ex:
            print("An error occurred:", ex)

# 4. You have to read a statement of the 1st exercise(Lists) and write a program with a dictionary. 

print("\n")
print("excercise 4:")

food_dict = {'eggs': 100, 'beef': 200, 'milk': 300, 'tomato': 400}
print(food_dict)

# 5. Try to execute problem of 10 'friends'

print("\n")
print("excercise 5:")

friends_years_dict = dict(zip(friends, years_of_birth))

print('\n')
for friend, year in friends_years_dict.items():
    print(f'{friend}: {year}')

# 6. Formulate and output an array with the size N (you choose), that consists of N odd numbers

print("\n")
print("excercise 6:")

N = int(input("Enter the size of the array: "))
odd_numbers = [i for i in range(1, 2*N, 2)]

print(odd_numbers)

# 7. Let be given N(you choose), and the first member A and difference D of arithmetic progression/sequence. Output the first N numbers of that sequence

print("\n")
print("excercise 7:")

N = int(input("Enter the amount of numbers to output: "))
A = int(input("Enter the first member: "))
D = int(input("Enter the difference of the progression: "))

progression = [A + i * D for i in range(N)]
print(f"The first {N} numbers of the progression: ", progression)

# 8. Let be given N(you choose), and the first member A and difference D of geometric progression/sequence. Output the first N numbers of that sequence

print("\n")
print("excercise 8:")

N = int(input("Enter the amount of numbers to output: "))
A = int(input("Enter the first member: "))
D = int(input("Enter the difference of the progression: "))

progression = [A * D**i for i in range(N)]
print(f"The first {N} numbers of the progression: ", progression)

# 9. Let be given N(you choose). Output an array of the size N that contains first N elements of Fibonnacci numbers

print("\n")
print("excercise 9:")

N = int(input("Enter the number of Fibonacci numbers to output: "))

def fibonacci_sequence(N):
    sequence = [0, 1]
    for i in range(2, N):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:N]

fib_sequence = fibonacci_sequence(N)
print(f"The first {N} Fibonacci numbers are: {fib_sequence}")

# 10. Let be given N(you choose but greater than 2), A and B. Write a program to output an array of the size N, first element of which is equal to A,the second - to B, and each subsequent element is equal to the sum of all the previous ones.

print("\n")
print("excercise 10:")

N = int(input("Enter the number greater than 2: "))
A = int(input("Enter the first number of the sequence: "))
B = int(input("Enter the last number of the sequence: "))

while (N <= 2):
  N = int(input("Enter the number again: "))

sequence = [A, B]
for i in range(2, N):
    sequence.append(sum(sequence))

print(f"Sequence of {N} numbers: {sequence}")