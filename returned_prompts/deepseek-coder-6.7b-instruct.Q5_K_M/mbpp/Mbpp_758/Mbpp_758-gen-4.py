
def unique_sublists(lst):
    # Initialize an empty dictionary
    dict_sublists = {}

    # Loop over the list
    for sublist in lst:
        # Convert the sublist to a tuple
        tuple_sublist = tuple(sublist)

        # If the tuple is not in the dictionary, add it with a value of 1
        if tuple_sublist not in dict_sublists:
            dict_sublists[tuple_sublist] = 1

        # If the tuple is already in the dictionary, increment its value by 1
        else:
            dict_sublists[tuple_sublist] += 1

    # Return the dictionary
    return dict_sublists

# Test the function
print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])) #{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

"""
This function works by first initializing an empty dictionary. It then loops over the input list and converts each sublist to a tuple. If the tuple is not already a key in the dictionary, it adds the key with a value of 1. If the tuple is already a key in the dictionary, it increments the value by 1. Finally, it returns the dictionary.
"""
<jupyter_output>
{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
<jupyter_text>
Question 3
<jupyter_code>
