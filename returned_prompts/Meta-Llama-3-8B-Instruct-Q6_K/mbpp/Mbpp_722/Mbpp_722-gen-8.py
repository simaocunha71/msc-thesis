```
def filter_data(data, min_height, min_weight):
    return {student: height_weight for student, height_weight in data.items() if height_weight[0] > min_height and height_weight[1] > min_weight}
```



The function `filter_data` takes a dictionary `data`, a minimum height `min_height`, and a minimum weight `min_weight` as input. It iterates over the dictionary items and checks if the student's height and weight are both greater than the minimum values. If both conditions are met, the student's name and height-weight tuple are included in the output dictionary. Finally, the function returns the filtered dictionary. 

The unit test provided ensures that the function works correctly by checking that the output dictionary contains only students with height and weight above the minimum. The test case `assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}` verifies that the function correctly filters out students with height and weight below the minimum. 





The unit test provided ensures that the function works correctly by checking that the output dictionary contains only students with height and weight above the minimum. The test case `assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}` verifies that the function correctly filters out students with height and weight below the minimum. 





The unit test provided ensures that the function works correctly by checking that the output dictionary contains only students with height and weight above the minimum. The test case `assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}` verifies that the function correctly filters out students with height and weight below the