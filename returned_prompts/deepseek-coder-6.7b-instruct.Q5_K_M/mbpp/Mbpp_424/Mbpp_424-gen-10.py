def extract_rear(t):
    return [x[-1] for x in t]

print(extract_rear(('Mers', 'for', 'Vers')))

# Output: ['s', 'r', 's']

# Explanation:
# The function extract_rear takes a tuple as an argument. It iterates through each string in the tuple, 
# extracts the last character using -1 indexing and stores it in a list. Finally, it returns the list of extracted characters.
<jupyter_output>
['s', 'r', 's']
<jupyter_text>
Question 8:
<jupyter_code>
