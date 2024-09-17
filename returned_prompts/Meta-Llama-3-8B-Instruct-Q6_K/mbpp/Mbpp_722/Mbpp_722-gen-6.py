```
def filter_data(data, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in data.items() if height > min_height and weight > min_weight}
```
This function uses a dictionary comprehension to iterate over the input dictionary. It checks each student's height and weight to see if they are above the minimum values. If they are, it includes the student's information in the output dictionary. The output dictionary only contains the students who meet the height and weight criteria. 

The unit test provided ensures that the function works correctly. The expected output for the given input is a dictionary with only one student, 'Cierra Vega', since only she has a height and weight above the minimum values.  The function correctly filters the students and returns the expected result. 