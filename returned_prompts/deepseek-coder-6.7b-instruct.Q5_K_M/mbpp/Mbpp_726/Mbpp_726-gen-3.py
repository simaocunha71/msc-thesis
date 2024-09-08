def multiply_elements(t):
    return tuple(t[i] * t[i+1] for i in range(len(t)-1))

assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""
This function works by using a generator expression to create a new tuple. The expression iterates over the indices i of the input tuple, and for each index i, it multiplies the element at that index and the next index. The result is a new tuple where each element is the product of the corresponding elements in the original tuple.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
