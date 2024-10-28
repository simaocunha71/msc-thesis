```
def concatenate_tuple(t):
    return '-'.join(map(str, t))
```


This function takes a tuple as an input and returns a string where each element of the tuple is concatenated by the '-' delimiter. The map function is used to convert each element to a string before joining. The unit test `assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'` ensures that the function works correctly. 

The output of this function would be 'ID-is-4-UTS' for the input tuple ("ID", "is", 4, "UTS"). 

The function works as follows:

- It takes a tuple 't' as an input.
- It uses map function to convert each element of the tuple into a string.
- It uses join function to concatenate each string element of the tuple with '-' delimiter.
- The resulting string is returned by the function. 

This function is useful when you need to concatenate elements of a tuple into a single string with a specific delimiter.  For example, you can use it to create a file name from a tuple of file name components. 

Note: The map function in Python is used to apply a given function to each item of an iterable (such as a list or tuple) and returns a list of the results. The str function is used to convert each element of the tuple to a string. The join function is used to concatenate each string element with '-' delimiter. 
```python
map(function, iterable)
```
This is a built-in Python function that applies a given function to each item of an iterable (such as a list or tuple) and returns a list of the results. The iterable can be a list, tuple, dictionary, or even a set. 

The str function is used to convert each element of the tuple to a string. This is necessary because the join function requires all elements to be strings. 

The join function is used to concatenate each string element with '-' delimiter. This function returns a string concatenated with the elements of an iterable, separated by a string separator. 
```python
'-'.join(map(str, t))
```
This will concatenate each element of the tuple 't' with '-' delimiter. The map function is used to convert each element to a string before joining. 
```python
'-' + '-'.join(map(str, t)) + '-'
```
This will add '-' before and after the concatenated string. 
```python
'-'.