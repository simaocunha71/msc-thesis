```
def index_minimum(lst):
    if not lst:
        raise ValueError("List is empty")
    return min(lst, key=lambda x: x[1])[0]
```
This function takes a list of tuples as an argument and returns the first value of the tuple with the smallest second value. It uses the built-in min function with a custom key function to find the tuple with the smallest second value, and then returns the first value of that tuple. If the list is empty, it raises a ValueError. 

The unit test `assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'` ensures that the function works correctly. It checks that the function returns 'Varsha', which is the first value of the tuple with the smallest second value (100) in the given list. 

The time complexity of this function is O(n), where n is the number of elements in the list, because it needs to iterate over the list once to find the minimum value. The space complexity is O(1), because it only uses a constant amount of space to store the minimum value and the first value of the minimum tuple. 
```
```python
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
assert index_minimum([]) == 'List is empty'
```



```python
def index_minimum(lst):
    if not lst:
        return "List is empty"
    return min(lst, key=lambda x: x[1])[0]
```
This function takes a list of tuples as an argument and returns the first value of the tuple with the smallest second value. It uses the built-in min function with a custom key function to find the tuple with the smallest second value, and then returns the first value of that tuple. If the list is empty, it returns the string "List is empty". 

The unit tests `assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'` and `assert index_minimum([]) == 'List is empty'` ensure that the function works correctly. They check that the function returns 'Varsha', which is the first value of the tuple with the smallest second value (100) in the given list, and 'List is empty' when the list is empty. 

The time complexity of this function is O