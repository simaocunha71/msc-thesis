def xor_tuples(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Both tuples must have the same length")

    return tuple(a ^ b for a, b in zip(t1, t2))

print(xor_tuples((10, 4, 6, 9), (5, 2, 3, 3)))
<jupyter_output>
(15, 6, 5, 10)
<jupyter_text>
**Problem 2**
<jupyter_code>
"""
