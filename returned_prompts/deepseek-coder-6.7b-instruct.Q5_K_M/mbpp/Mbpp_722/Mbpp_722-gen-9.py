def filter_data(students, min_height, min_weight):
    return {k: v for k, v in students.items() if v[0] >= min_height and v[1] >= min_weight}

print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))

This function uses dictionary comprehension to create a new dictionary. It only includes the key-value pairs from the original dictionary where the height and weight are both greater than or equal to the minimum height and weight.

Alternative solution:
You can also use the built-in filter() function. 

def filter_data(students, min_height, min_weight):
    return dict(filter(lambda s: s[1][0] >= min_height and s[1][1] >= min_weight, students.items()))

print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))
"""

# Solution 2:
"""
