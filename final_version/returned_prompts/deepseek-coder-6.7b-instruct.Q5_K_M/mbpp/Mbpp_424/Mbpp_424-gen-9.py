def extract_rear(tup):
    return [s[-1] for s in tup]

print(extract_rear(('Mers', 'for', 'Vers')))

#Output: ['s', 'r', 's']

#Explanation: The function extract_rear takes a tuple as input. It uses list comprehension to iterate over each string in the tuple. For each string, it extracts the last character by indexing using [-1] and adds it to the list. The function returns the resulting list of extracted characters.

#For example, for the input ('Mers', 'for', 'Vers'), the function returns ['s', 'r', 's'].
<jupyter_output>
['s', 'r', 's']
<jupyter_text>
