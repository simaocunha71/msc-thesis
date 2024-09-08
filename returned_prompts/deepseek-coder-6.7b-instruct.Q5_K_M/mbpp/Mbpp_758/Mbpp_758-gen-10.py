
def unique_sublists(lst):
    result = {}
    for sublist in lst:
        if type(sublist) is list:
            sublist = tuple(sublist)
        if sublist in result:
            result[sublist] += 1
        else:
            result[sublist] = 1
    return result

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))

# Output: {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

"""
In the function unique_sublists, we iterate through the input list. 
If we encounter a list, we convert it to a tuple and check if it is already a key in the result dictionary. 
If it is, we increment the value associated with that key by 1. 
If it isn't, we add a new key-value pair to the dictionary with the key being the tuple and the value being 1. 
Finally, we return the result dictionary.
"""
<jupyter_output>
{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
<jupyter_text>
Question 6
<jupyter_code>
