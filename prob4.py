# lists of random letters for testing code
l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
l2 = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
# letters f-j should be returned

# lambda function that compares letters and returns the intersecting letters
intersecting = list(filter(lambda x: x in l1, l2))

# print result
print(intersecting)