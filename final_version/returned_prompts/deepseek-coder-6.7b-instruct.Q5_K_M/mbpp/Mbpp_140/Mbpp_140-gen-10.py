
def extract_singly(list_of_lists):
    result = []
    for sublist in list_of_lists:
        if isinstance(sublist, tuple):
            result.extend(sublist)
        else:
            result.append(sublist)
    return set(result)

print(extract_singly([(3, 4, 5), 4, 5, 7, 1]))

# Output: {1, 3, 4, 5, 7}

"""
In the above code, we iterate through the list and check the type of each element. If it's a tuple, we extend the result list by the elements of the tuple. If not, we just append the element to the result list. Finally, we convert the result list to a set to remove duplicates and return it.
"""
<jupyter_output>
{1, 3, 4, 5, 7}
<jupyter_text>
Problem 2
<jupyter_code>
