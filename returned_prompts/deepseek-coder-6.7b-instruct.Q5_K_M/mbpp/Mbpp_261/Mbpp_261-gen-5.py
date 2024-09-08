def division_elements(tup1, tup2):
    return tuple([x1/x2 for x1, x2 in zip(tup1, tup2)])

print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)))

"""
Output:
(2.0, 2.0, 2.0, 3.0)
"""

"""
Explanation:
The function 'division_elements' takes in two tuples as arguments. It uses the built-in 'zip' function to iterate over the elements of the two tuples simultaneously. It then uses a list comprehension to divide the elements of the first tuple by the corresponding elements of the second tuple. These divided elements are then returned as a tuple.
"""
<jupyter_output>
(2.0, 2.0, 2.0, 3.0)
<jupyter_text>
Question 2
<jupyter_code>
