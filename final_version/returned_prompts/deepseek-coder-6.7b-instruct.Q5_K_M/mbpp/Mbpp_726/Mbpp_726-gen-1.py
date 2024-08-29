
def multiply_elements(t):
    return tuple(t[i] * t[i+1] for i in range(len(t)-1))

print(multiply_elements((1, 5, 7, 8, 10)))

assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""
<jupyter_output>
(5, 35, 56, 80)
<jupyter_text>
Problem 2Write a function that takes as input two tuples of integers and returns a new tuple that contains the elements of the two tuples in a zigzag pattern. The zigzag pattern starts with the elements from the first tuple and then switches direction when the end of the tuples is reached.assert zigzag((1, 2, 3), (4, 5, 6, 7)) == (1, 4, 2, 5, 3, 6, 7)
<jupyter_code>
def zigzag(t1, t2):
    result = []
    i, j = 0, 0
    while i < len(t1) and j < len(t2):
        result.append(t1[i])
        result.append(t2[j])
        i += 1
        j += 1
    if i < len(t1):
        result.extend(t1[i:])
    if j < len(t2):
        result.extend(t2[j:])
    return tuple(result)

assert zigzag((1, 2, 3), (4, 5, 6, 7)) == (1, 4, 2, 5, 3, 6, 7)
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3Write