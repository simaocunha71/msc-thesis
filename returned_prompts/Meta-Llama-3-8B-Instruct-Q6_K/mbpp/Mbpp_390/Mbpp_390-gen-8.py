```
def add_string(lst, fmt):
    return [fmt.format(i) for i in lst]
```


In this problem, we are asked to create a function that takes a list of elements and a format string as inputs, and returns a new list where each element from the original list is formatted according to the given format string. 

The provided unit test `assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']` suggests that the function should replace the placeholder in the format string with each element from the list and return the resulting list.

Here, we can use Python's built-in `format` method to replace the placeholder with each element from the list. The `format` method takes an iterable of arguments as its second argument, and replaces the placeholders in the format string with the corresponding elements from the iterable. 

For example, if we have a format string `'temp{0}'` and a list `[1,2,3,4]`, the `format` method will replace the `{0}` placeholder with each element from the list, resulting in the list `['temp1', 'temp2', 'temp3', 'temp4']`. 

We can use a list comprehension to apply the `format` method to each element from the list and create the new list. Here's the solution:
```
def add_string(lst, fmt):
    return [fmt.format(i) for i in lst]
```


This function takes a list `lst` and a format string `fmt` as inputs, and returns a new list where each element from the original list is formatted according to the given format string. The `format` method is used to replace the placeholder in the format string with each element from the list, and the resulting list is returned. 

For example, if we call `add_string([1,2,3,4],'temp{0}')`, the function will return `['temp1', 'temp2', 'temp3', 'temp4']`. 
```python
print(add_string([1,2,3,4],'temp{0}'))  # Output: ['temp1', 'temp2', 'temp3', 'temp4']
``` 
This solution passes the provided unit test. 
```python
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4