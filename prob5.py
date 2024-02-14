# list of numbers to test code
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# constant
n = 3

# lambda function that raises each num in list to the power of n
exponential_mapping = list(map(lambda x: x**n, numbers))

# print result
print(exponential_mapping)