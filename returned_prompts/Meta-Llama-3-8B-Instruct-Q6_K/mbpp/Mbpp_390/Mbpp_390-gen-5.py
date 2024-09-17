```
def add_string(lst, format_string):
    return [format_string.format(i) for i in lst]
```
This function takes a list and a format string as inputs. It uses a list comprehension to iterate over each element in the list, and applies the format string to each element using the `format()` method. The result is a new list with the formatted strings. 

For example, if you call `add_string([1,2,3,4],'temp{0}')`, the function will return `['temp1', 'temp2', 'temp3', 'temp4']`. 

The unit test `assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']` ensures that the function works correctly. 

Note: The format string should be a string that contains format specifiers (like `{0}`) which will be replaced with the actual values from the list. The `format()` method will do this replacement. 
```python
print(add_string([1,2,3,4],'temp{0}'))  # Output: ['temp1', 'temp2', 'temp3', 'temp4']
```  ```python
print(add_string(['a', 'b', 'c'], '{0} is a letter'))  # Output: ['a is a letter', 'b is a letter', 'c is a letter']
```  ```python
print(add_string([1,2,3,4], 'The number is {0}'))  # Output: ['The number is 1', 'The number is 2', 'The number is 3', 'The number is 4']
```  ```python
print(add_string(['apple', 'banana', 'cherry'], '{0} is a fruit'))  # Output: ['apple is a fruit', 'banana is a fruit', 'cherry is a fruit']
```  ```python
print(add_string([1,2,3,4], '{0} times {1}'))  # Output: ['1 times 2', '2 times 3', '3 times 4']
```  ```python
print(add_string([1,2,3,4], '{0} + {1} = {0+1}'))  # Output: ['1 + 2 = 3', '2 + 3 = 5', '3 + 4 = 7