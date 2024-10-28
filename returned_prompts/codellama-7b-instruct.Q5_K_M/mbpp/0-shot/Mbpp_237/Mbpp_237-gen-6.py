"""
def check_occurences(my_list):
    # Create an empty dictionary to store the counts
    counts = {}

    # Iterate through the list of tuples
    for tup in my_list:
        # If the tuple is not in the dictionary, add it and set its count to 1
        if tup not in counts:
            counts[tup] = 1
        # Otherwise, increment its count
        else:
            counts[tup] += 1

    return counts
"""
