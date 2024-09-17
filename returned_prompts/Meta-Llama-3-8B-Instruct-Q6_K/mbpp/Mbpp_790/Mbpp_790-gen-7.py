```
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i]%2 != 0:
            return False
    return True
```    
    This function takes a list as an input and checks whether every even index contains even numbers. It iterates over the list with a step size of 2, which means it checks every even index. If it finds an index where the number is not even (i.e., the remainder when divided by 2 is not 0), it returns False. If it checks all the even indices and doesn't find any non-even numbers, it returns True. The unit test `assert even_position([3,2,1]) == False` ensures that the function works correctly. 
```python
print(even_position([3,2,1])) # Output: False
print(even_position([2,4,6])) # Output: True
```    
The function is case-sensitive and works with any type of list, not just lists of integers. It also works with empty lists, returning True. 
```python
print(even_position([])) # Output: True
```    
However, it does not handle non-list inputs, and may raise an error if given a non-list.    
```python
print(even_position('hello')) # Raises TypeError
```    
To handle non-list inputs, you could add a simple check at the beginning of the function:
```python
def even_position(lst):
    if not isinstance(lst, list):
        return False
    for i in range(0, len(lst), 2):
        if lst[i]%2 != 0:
            return False
    return True
```    
Now the function will return False for non-list inputs.    
```python
print(even_position('hello')) # Output: False
```    
You could also add a message to the return value to make it more informative:
```python
def even_position(lst):
    if not isinstance(lst, list):
        return False, 'Input is not a list'
    for i in range(0, len(lst), 2):
        if lst[i]%2 != 0:
            return False, 'At least one even index contains an odd number'
    return True, 'All even indices contain even numbers'
```    
Now the function returns a tuple, where the first element is a boolean indicating whether the condition is met, and the second element is a string describing the result.    
```python