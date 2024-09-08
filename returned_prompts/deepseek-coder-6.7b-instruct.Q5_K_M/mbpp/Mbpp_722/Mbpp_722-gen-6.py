```python
def filter_data(data, min_height, min_weight):
    return {k: v for k, v in data.items() if v[0] >= min_height and v[1] >= min_weight}

print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))
```

This function uses a dictionary comprehension to create a new dictionary that only includes key-value pairs where the value (which is a tuple of height and weight) has a height and weight that is both greater than or equal to the min_height and min_weight, respectively.

The dictionary comprehension works by iterating over each key-value pair in the input data. If the student’s height and weight are both greater than or equal to the minimum, they are included in the new dictionary. If not, they are not. This is determined by the condition in the if statement, which checks if each student’s height and weight are both greater than or equal to the minimum.

The function returns this new dictionary.
"""

"""

"""
