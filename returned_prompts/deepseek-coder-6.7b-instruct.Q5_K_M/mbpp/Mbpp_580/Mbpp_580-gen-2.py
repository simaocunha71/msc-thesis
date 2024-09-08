
def extract_even(tup):
    result = []
    for i in tup:
        if isinstance(i, tuple):
            new_tuple = extract_even(i)
            if new_tuple:  # if new_tuple is not empty
                result.append(new_tuple)
        elif i % 2 == 0:
            result.append(i)
    return tuple(result)

print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)))

# Output:
# (4, (6, (2, 4)), 6, 8)

# This solution uses recursion to handle the nested tuples. It checks for each element of the tuple if it is a tuple. If it is a tuple, it calls itself with this tuple as an argument. If the result of this call is not empty, it appends this result to the result list. If the current element is not a tuple and it is an even number, it appends it to the result list. Finally, it converts the result list to a tuple and returns it.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4
<jupyter_code>
