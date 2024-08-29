
def index_multiplication(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        temp = []
        for j in range(len(tup1[i])):
            temp.append(tup1[i][j] * tup2[i][j])
        result.append(tuple(temp))
    return tuple(result)

print(index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))))

# Output: ((6, 21), (12, 45), (2, 9), (7, 30))

"""
Explanation: 
This function works by iterating over each element in the given tuples at the same index. For each element, it multiplies the values at the same index in the two tuples and appends the result to a new tuple. This new tuple is then appended to a list which is returned as the final result.
"""

# 2. Write a Python function to find the sum of all elements in a list using recursion.

