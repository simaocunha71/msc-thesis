def multiply_elements(tup):
    return tuple(tup[i]*tup[i+1] for i in range(len(tup)-1))

print(multiply_elements((1, 5, 7, 8, 10)))

# Output: (5, 35, 56, 80)

"""
Explanation:
The function takes a tuple as input. Then it uses list comprehension to iterate over the tuple and multiply each element by the next one. The result is then converted back into a tuple and returned.
"""
<jupyter_output>
(5, 35, 56, 80)
<jupyter_text>
Problem 2:
<jupyter_code>
