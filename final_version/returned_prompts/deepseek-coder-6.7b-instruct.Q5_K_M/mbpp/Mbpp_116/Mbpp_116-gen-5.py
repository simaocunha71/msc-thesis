def tuple_to_int(tup):
    return int(''.join(map(str, tup)))

print(tuple_to_int((1,2,3)))

"""
Explanation:
We use the map function to convert all elements in the tuple to strings. Then we join these strings together using the join method, which is used to concatenate the elements of a list.
Finally, we convert the resulting string to an integer using the int function.
"""

"""
