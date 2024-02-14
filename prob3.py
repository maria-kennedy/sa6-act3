# list of numbers to test code
numbers = [1, 5, 3, 9, 2, 7, 6, 4, 8, 10, 11, 17, 20]

# lambda function to compare two numbers and return the greater of the two
checker = lambda x, y: x if x > y else y

# function takes a list of numbers and a lambda function as arguments
def find_max(numbers, checker):
    max = numbers[0]
    for i in numbers:
        max = checker(max, i)
    return max 

# print result
print(find_max(numbers, checker))



