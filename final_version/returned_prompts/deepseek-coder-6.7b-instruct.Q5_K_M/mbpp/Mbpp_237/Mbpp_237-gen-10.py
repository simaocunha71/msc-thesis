
def check_occurences(tuples):
    # Create an empty dictionary to store the counts
    counts = {}

    # Iterate over each tuple in the list
    for tup in tuples:
        # If the tuple is already in the dictionary, increment its count
        if tup in counts:
            counts[tup] += 1
        # If the tuple is not in the dictionary, add it with a count of 1
        else:
            counts[tup] = 1

    # Return the counts dictionary
    return counts

print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))  # Should return {(1, 3): 2, (2, 5): 2, (3, 6): 1}

This function works by iterating over each tuple in the input list, and checking if it's already in the counts dictionary. If it is, it increments the count for that tuple; if it's not, it adds the tuple to the dictionary with a count of 1. Finally, it returns the counts dictionary.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
