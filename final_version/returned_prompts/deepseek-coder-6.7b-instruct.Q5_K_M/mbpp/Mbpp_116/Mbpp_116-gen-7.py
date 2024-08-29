def tuple_to_int(tup):
    return int(''.join(map(str, tup)))

print(tuple_to_int((1,2,3))) #==123

Explanation:
This solution uses the built-in map function to convert all the numbers in the tuple to strings, then joins them together with no separator in between. This results in a single string of numbers. Finally, it converts this string to an integer and returns it.
"""

