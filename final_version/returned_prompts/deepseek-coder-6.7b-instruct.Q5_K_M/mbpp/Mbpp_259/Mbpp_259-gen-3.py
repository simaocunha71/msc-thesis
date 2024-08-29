
def maximize_elements(t1, t2):
    return tuple(max(a, b) for a, b in zip(t1, t2))

print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))))

"""
In this function, we use the built-in zip function to pair up the elements from the two tuples. Then, we use the built-in max function to select the maximum value from each pair. 

We return the result as a new tuple.

This function assumes that the two tuples are of the same length and that each element in the tuples is itself a tuple of two elements.
"""
<jupyter_output>
((6, 7), (4, 9), (2, 9), (7, 10))
<jupyter_text>
Problem 3
<jupyter_code>
