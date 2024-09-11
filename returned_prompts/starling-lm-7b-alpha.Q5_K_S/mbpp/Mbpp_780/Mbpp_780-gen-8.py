def find_combinations(tup_list):
    result = []
    for tup1 in tup_list:
        for tup2 in tup_list:
            result.append((tup1[0]+tup2[0], tup1[1]+tup2[1]))
    return result

find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)])

"""
Explanation:
The problem asks to find all the tuples of two elements with sums that are in the given list of tuples.
The function creates an empty list called result to store the tuples with sums.
It then iterates through the list of tuples with a for loop. For each tuple in the list, it iterates through the list again with another for loop.
For each pair of tuples, it adds the first elements of the tuples to create a new tuple of sums, and appends the tuple to the result list.
Finally, it returns the result list containing all the tuples of sums.
"""

# Python3 program to find all
# combinations of sums with
# tuples in the given tuple
# list.

# Function to find all
# combinations of sums
def find_combinations(tup_list):

    # Create an empty result
    result = []

    # Iterate through the
    # list of tuples
    for tup1 in tup_list:
        for tup2 in tup_list:

            # Add the first
            # elements of the
            # tuples to create
            # a new tuple
            # of sums
            result.append((tup1[0]+tup2[0],
                           tup1[1]+tup2[1]))

    # Return the result
    return result

# Driver code
tup_list = [(2, 4), (6, 7), (5, 1), (6, 10)]

# Function call
print(find_combinations(tup_list))

"""
Explanation:
The function find_combinations takes a list of tuples