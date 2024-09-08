
def extract_even(tup):
    result = []
    for i in tup:
        if type(i) == tuple:
            new_tuple = extract_even(i)
            if new_tuple:
                result.append(new_tuple)
        elif i % 2 == 0:
            result.append(i)
    return tuple(result)


print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)))

# Output: (4, (6, (2, 4)), 6, 8)

"""
Here, the function extract_even takes a tuple as an argument. Then it iterates over the elements of the tuple. If the element is a tuple, it calls itself with the element as the argument. The returned result is appended to the result list if it's not empty. If the element is not a tuple and is an even number, it is appended to the result list. The function finally returns the result list as a tuple.
"""
<jupyter_output>
(4, (6, (2, 4)), 6, 8)
<jupyter_text>
Question 2
<jupyter_code>
