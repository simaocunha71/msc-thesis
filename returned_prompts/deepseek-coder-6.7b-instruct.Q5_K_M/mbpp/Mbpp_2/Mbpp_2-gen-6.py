
def similar_elements(l1, l2):
    return set(l1) & set(l2)

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))

# OR

def similar_elements(l1, l2):
    return [value for value in l1 if value in l2]

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))

Both of these functions will return the set of common elements between the two lists. The first function uses the set intersection operator (&) to find common elements, while the second function uses list comprehension and the 'in' operator.
<jupyter_output>
<empty_output>
<jupyter_text>
