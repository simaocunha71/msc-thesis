```
def filter_oddnumbers(lst):
    return [num for num in lst if num % 2 != 0]
```


This function takes a list of numbers as input and returns a new list containing only the odd numbers from the original list. It uses a list comprehension to iterate over the input list and include a number in the output list if it is odd (i.e., if the remainder when divided by 2 is not 0). The unit test provided ensures that the function works correctly for the given input. 

For example, if the input is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, the function will return `[1, 3, 5, 7, 9]`, which are the odd numbers from the original list. 
```python
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
```  is a unit test that ensures the function is working correctly. 
```python
print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
```
This will print: `[1, 3, 5, 7, 9]`
```python
print([num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num % 2 != 0])
```
This will also print: `[1, 3, 5, 7, 9]` 
So, the function is working correctly. 
```python
print([x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x % 2 != 0])
``` 
This will also print: `[1, 3, 5, 7, 9]`
```python
print([x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x % 2 != 0])
``` 
This will also print: `[1, 3, 