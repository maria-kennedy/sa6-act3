# test case
number = 1006

#lambda function
digit_sum = lambda x: sum([int(i) for i in str(x)])

# print result
print(digit_sum(number))