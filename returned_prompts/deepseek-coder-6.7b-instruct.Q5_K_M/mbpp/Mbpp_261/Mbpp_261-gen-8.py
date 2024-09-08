
def division_elements(t1, t2):
    return tuple(a / b for a, b in zip(t1, t2))

print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)))

# Output: (2.0, 2.0, 2.0, 3.0)

"""
The function works by iterating over the two input tuples simultaneously using the zip function. For each pair of corresponding elements in the two tuples, it performs the division operation. The resulting values are collected into a new tuple using a tuple comprehension.
"""
<jupyter_output>
(2.0, 2.0, 2.0, 3.0)
<jupyter_text>
Question 4
<jupyter_code>
