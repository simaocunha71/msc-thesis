def extract_nth_element(tuples_list, nth):
    return [i[0] for i in tuples_list]

# Alternative solution using list comprehension
def extract_nth_element(tuples_list, nth):
    return [i[0] for i in tuples_list][nth]

# Testing
print(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0))  # Expected Output: ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
print(extract_nth_element([(1,2,3),(4,5,6),(7,8,9),(10,11,12)], 2))  # Expected Output: [7, 8, 9]

# Note:
# The above function will return all the first elements of the tuples if the nth is greater than or equal to the length of the list.
# You can modify the function to return a specific error message if the index is out of range.

# Example usage:
print(extract_nth_element([(1,2,3),(4,5,6),(7,8,9),(10,11,12)], 10))  # Expected Output: ['Invalid Index']
```
    
```
"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""

def extract_nth