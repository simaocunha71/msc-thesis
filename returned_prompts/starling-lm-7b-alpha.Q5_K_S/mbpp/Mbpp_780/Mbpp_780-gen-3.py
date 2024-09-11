def find_combinations(tuples):
    result = []
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            result.append((tuples[i][0]+tuples[j][0], tuples[i][1]+tuples[j][1]))
    return result

# assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
# print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))

"""
The function finds the sum of the first elements and second elements of the tuples and adds them to the result list. It does this by iterating over the tuples and for each tuple in the list, it iterates over the rest of the tuples and adds the sums to the result list.
"""

# This function can be used to find the combinations of sums with tuples in the given tuple list. It takes a list of tuples as input and returns a list of tuples, where each tuple contains the sum of the first elements and the sum of the second elements of two tuples from the input list.

# Here is an example of how to use the function:
# find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)])
# This will return [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]. Each tuple represents the sum of the first elements and the sum of the second elements of two tuples from the input list.

# The function works by iterating over the tuples and for each tuple in the list, it iterates over the rest of the tuples and adds the sums to the result list.

# Note that the function assumes that all tuples in the input