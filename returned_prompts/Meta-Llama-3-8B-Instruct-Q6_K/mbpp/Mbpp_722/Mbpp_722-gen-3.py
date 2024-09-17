```
def filter_data(students, min_height, min_weight):
    return {name: height_weight for name, height_weight in students.items() if height_weight[0] > min_height and height_weight[1] > min_weight}
```
The function `filter_data` takes three parameters: `students`, `min_height`, and `min_weight`. It iterates over the items in the `students` dictionary and checks if the height and weight of each student are above the minimum. If they are, it includes the student's name and height/weight in the output dictionary. The function then returns the dictionary of students that meet the criteria.

The unit test `assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}` ensures that the function correctly filters the students based on the given minimum height and weight. The expected output is a dictionary with only 'Cierra Vega' as the key, since she is the only student with height and weight above the minimum.