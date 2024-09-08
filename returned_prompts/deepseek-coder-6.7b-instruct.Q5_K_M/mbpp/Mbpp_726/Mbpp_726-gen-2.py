def multiply_elements(t):
    return tuple(t[i] * t[i+1] for i in range(len(t)-1))

print(multiply_elements((1, 5, 7, 8, 10)))

# Output:
# (5, 35, 56, 80)

# This solution uses a simple list comprehension to generate the new tuple. The list comprehension iterates over the input tuple and for each index i, it multiplies the element at index i with the element at index i+1.

# The time complexity of this solution is O(N), where N is the length of the input tuple. This is because it makes a single pass over the input tuple. The space complexity is also O(N), as it creates a new tuple that is of length N.
<jupyter_output>
(5, 35, 56, 80)
<jupyter_text>
2. Given a list of tuples, write a Python function that returns the list of tuples, but with the integer values replaced by their ordinal numbers starting from 1.
<jupyter_code>
