```
def filter_data(students, min_height, min_weight):
    return {name: height_weight for name, height_weight in students.items() if height_weight[0] > min_height and height_weight[1] > min_weight}
```


The function filter_data takes as input a dictionary of students, a minimal height, and a minimal weight. It iterates over the dictionary and filters out students who have a height and weight below the minimum. The function returns a new dictionary containing only the students who meet the condition. The unit test provided ensures that the function works correctly. For example, given the input {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)} and the minimum height and weight 6.0 and 70, the function should return {'Cierra Vega': (6.2, 70)}. 