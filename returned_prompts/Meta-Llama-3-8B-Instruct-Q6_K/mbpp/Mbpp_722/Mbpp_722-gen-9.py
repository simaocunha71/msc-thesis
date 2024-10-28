```
def filter_data(students, min_height, min_weight):
    return {student: data for student, data in students.items() if data[0] > min_height and data[1] > min_weight}
```
This function iterates over each student in the input dictionary. For each student, it checks if their height and weight are above the minimum. If they are, it includes the student in the output dictionary. The function returns this dictionary. The unit test provided ensures that the function works correctly.