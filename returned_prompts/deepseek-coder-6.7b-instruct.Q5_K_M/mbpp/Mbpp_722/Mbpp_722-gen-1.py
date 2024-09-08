Here is the Python code to solve the problem:

```python
def filter_data(students, min_height, min_weight):
    return {name: details for name, details in students.items() if details[0] >= min_height and details[1] >= min_weight}

students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
min_height = 6.0
min_weight = 70
print(filter_data(students, min_height, min_weight))
```

The function `filter_data` takes the dictionary `students`, and the minimal height and weight as inputs. It uses dictionary comprehension to create a new dictionary where the key is the student's name and the value is the student's details (height, weight). The condition for including a student in the new dictionary is that their height and weight must be greater than or equal to the minimum height and weight.

When we run the program, it will print the filtered dictionary:

`{'Cierra Vega': (6.2, 70)}`

This shows that only 'Cierra Vega' has a height and weight greater than or equal to the minimum height (6.0) and weight (70), while the other students are filtered out.
"""

