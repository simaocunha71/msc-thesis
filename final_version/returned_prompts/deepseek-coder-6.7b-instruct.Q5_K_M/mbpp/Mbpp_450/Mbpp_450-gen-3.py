def extract_string(lst, size):
    return [s for s in lst if len(s) > size]

print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8))

# Output: ['practice', 'solution']

# Explanation: The function extract_string goes through each string in the list. If the length of the string is more than the given size, it is added to the output list. The output list is then returned.
<jupyter_output>
['practice', 'solution']
<jupyter_text>
Exercise 3:Write a Python function that takes a list of numbers and returns a list of only the even numbers.
<jupyter_code>
