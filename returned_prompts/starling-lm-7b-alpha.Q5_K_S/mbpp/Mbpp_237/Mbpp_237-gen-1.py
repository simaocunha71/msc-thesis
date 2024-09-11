"""
def check_occurences(tuples):
    # Create an empty dictionary to store the result
    result = dict()

    # Iterate through the tuples
    for tup in tuples:
        # If the tuple is already in the dictionary, increment the count
        if tup in result:
            result[tup] += 1
        # If the tuple is not in the dictionary, add it with a count of 1
        else:
            result[tup] = 1

    return result
"""

# Time complexity: O(n)
# Space complexity: O(n)

