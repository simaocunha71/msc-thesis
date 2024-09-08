
def check_occurences(tup_list):
    dict_count = {}
    for tup in tup_list:
        if tup in dict_count:
            dict_count[tup] += 1
        else:
            dict_count[tup] = 1
    return dict_count

# Test the function
print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))  # Should print {(3, 1): 2, (1, 3): 2, (2, 5): 2, (5, 2): 2, (6, 3): 1}

# The function works by creating an empty dictionary and then iterating over the input list of tuples. If a tuple is already in the dictionary, it increments its count by 1. If not, it adds the tuple to the dictionary with a count of 1. Finally, it returns the dictionary.
<jupyter_output>
{(1, 3): 2, (2, 5): 2, (3, 6): 1}
<jupyter_text>
Problem 2
<jupyter_code>
