def multiply_elements(t):
    return tuple(t[i] * t[i + 1] for i in range(len(t) - 1))

print(multiply_elements((1, 5, 7, 8, 10)))
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
<jupyter_output>
(5, 35, 56, 80)
<jupyter_text>
Problem 2
<jupyter_code>
