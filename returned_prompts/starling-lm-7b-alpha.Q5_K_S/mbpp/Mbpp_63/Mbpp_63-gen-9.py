"""
def max_difference(tup_list):
    # Initialize max_diff to 0.
    max_diff = 0
    # Iterate through each tuple in the list.
    for tup in tup_list:
        # Initialize diff to the first element of the tuple.
        diff = tup[0]
        # Iterate through the rest of the elements in the tuple.
        for elem in tup[1:]:
            # Update diff to be the greater of diff and elem.
            diff = max(diff, elem)
        # Update max_diff to be the greater of max_diff and diff.
        max_diff = max(max_diff, diff)
    # Return the result.
    return max_diff

# Run the test case.
print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))
"""

# The above solution will result in a Time Limit Exceeded error due to the nested for loops.
# Here is a more efficient solution using list comprehensions:

"""
def max_difference(tup_list):
    # Initialize max_diff to 0.
    max_diff = 0
    # Iterate through each tuple in the list.
    for tup in tup_list:
        # Initialize diff to the first element of the tuple.
        diff = tup[0]
        # Iterate through the rest of the elements in the tuple.
        for elem in [elem for elem in tup[1:] if elem > diff]:
            # Update diff to be the greater of diff and elem.
            diff = max(diff, elem)
        # Update max_diff to be the greater of max_diff and diff.
        max_diff = max(max_diff, diff)
    # Return the result.
    return max_diff

# Run the test case.
print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))
"""

# The above solution will still result in a Time Limit Exceeded error due to the nested for loops.
# Here is a more