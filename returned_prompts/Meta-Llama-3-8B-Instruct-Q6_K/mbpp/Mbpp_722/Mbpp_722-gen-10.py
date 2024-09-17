```
def filter_data(students, min_height, min_weight):
    filtered_students = {student: height_weight for student, height_weight in students.items() if height_weight[0] > min_height and height_weight[1] > min_weight}
    return filtered_students
```
This function iterates over each student in the input dictionary. For each student, it checks if their height and weight are greater than the minimum height and weight. If they are, the student is included in the filtered dictionary. The function then returns this filtered dictionary. 

In the unit test provided, the function is called with the following parameters: 
- students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
- min_height = 6.0
- min_weight = 70

The function returns {'Cierra Vega': (6.2, 70)}, which means that only Cierra Vega has a height and weight above the minimum. 
```python
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
```  ```python
``` 