# list of strings, using fruits as an example
fruits = ['apple', 'banana', 'pear', 'watermelon', 'cherry']

# sort the list of strings by length
ordered_fruits = sorted(fruits, key=lambda x: len(x))

# print result
print(ordered_fruits)