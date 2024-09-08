def extract_rear(t):
    return [s[-1] for s in t]

print(extract_rear(('Mers', 'for', 'Vers')))

# Output: ['s', 'r', 's']

#Explanation: The function extract_rear takes a tuple of strings as input and returns a list of characters. It uses a list comprehension to iterate over each string in the tuple and append the last character (s[-1]) to the list.
<jupyter_output>
['s', 'r', 's']
<jupyter_text>
Question 3:
<jupyter_code>
