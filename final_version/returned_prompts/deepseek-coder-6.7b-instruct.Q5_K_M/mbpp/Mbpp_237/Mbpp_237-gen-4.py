
def check_occurences(lst):
    result = {}
    for tup in lst:
        if tup in result:
            result[tup] += 1
        else:
            result[tup] = 1
    return result

assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2, (6, 3): 1}
"""
The function works by iterating over the list of tuples. For each tuple, it checks if the tuple is already a key in the dictionary. If it is, it increments the associated value by 1. If it isn't, it adds the tuple as a key with a value of 1. Finally, it returns the resulting dictionary.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Task 2
<jupyter_code>
