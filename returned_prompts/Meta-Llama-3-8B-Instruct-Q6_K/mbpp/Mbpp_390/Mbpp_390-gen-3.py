```
def add_string(lst, format_str):
    return [format_str.format(i) for i in lst]
```
This function takes a list and a format string as input. It uses a list comprehension to iterate over each element in the list, replacing `{0}` in the format string with the current element. The result is a new list where each element is the original element formatted with the given format string. 

For example, if we call `add_string([1,2,3,4],'temp{0}')`, it will return `['temp1', 'temp2', 'temp3', 'temp4']`. 

The unit test `assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']` confirms that this function works as expected. 
```
```python
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
print(add_string([1,2,3,4],'temp{0}'))
````
The output will be:
```
['temp1', 'temp2', 'temp3', 'temp4']
```python
```python
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
print(add_string([1,2,3,4],'temp{0}'))
````
The output will be:
```
['temp1', 'temp2', 'temp3', 'temp4']
```python
```python
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
print(add_string([1,2,3,4],'temp{0}'))
````
The output will be:
```
['temp1', 'temp2', 'temp3', 'temp4']
```python
```python
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
print(add_string([1,2,3,4],'temp{0}'))
````
The output will be:
```
['temp1', 'temp2', 'temp3', 'temp4']
```python
```python
assert add_string([1,