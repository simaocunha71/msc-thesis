```
def extract_string(lst, size):
    return [item for item in lst if len(item) == size]
```
This function takes a list of strings and a size as input, and returns a new list containing only the strings from the input list that have the specified size.

For example, if you call `extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)`, it will return `['practice', 'solution']` because these are the strings in the input list that have a length of 8. 

The unit test `assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']` ensures that the function works correctly for this specific input. 

The function uses a list comprehension to iterate over the input list and select the strings that have the specified size. The `len(item)` function is used to get the length of each string, and the `if` condition is used to filter the strings based on their length. 
```python
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
```  ```python
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,4)==['list', 'exercises']
```  ```python
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['exercises']
```  ```python
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,3)==['list']
```  ```python
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,1)==[]
```  ```python
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,0)==[]
```  ```python
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,2)==['is', 'so']
```  ```python
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,5)==['exer', 'prac']
```  ```python
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==[]
```  ```python
assert extract_string(['Python', 'list', 'exercises