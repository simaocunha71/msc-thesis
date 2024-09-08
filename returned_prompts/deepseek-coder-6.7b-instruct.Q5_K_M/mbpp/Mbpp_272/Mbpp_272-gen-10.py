def rear_extract(lst):
    return [x[-1] for x in lst]

print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]))

# Output: [21, 20, 19]

# Explanation:
# The function rear_extract takes a list of tuples as input.
# It uses a list comprehension to create a new list where each element is the last element of the corresponding input tuple.
# This is achieved by indexing with -1 (which is the last element in a sequence in Python), and the result is returned.
<jupyter_output>
[21, 20, 19]
<jupyter_text>
Exercise 4: Write a Python function that takes a list of integers and returns a dictionary where the keys are the integers and the values are their squares.
<jupyter_code>
