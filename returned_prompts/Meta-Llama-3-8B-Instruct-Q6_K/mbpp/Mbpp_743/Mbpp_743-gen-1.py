```
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]
```
This function takes a list and an integer n as input, and returns the list rotated to the right by n positions. The rotation is done by slicing the list into two parts, the last n elements and the rest of the list, and then concatenating them in reverse order. The modulus operation is used to ensure that n is within the range of the list length, in case n is greater than the list length. 

For example, if the input list is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and n is 3, the function will return [8, 9, 10, 1, 2, 3, 4, 5, 6, 7], which is the original list rotated to the right by 3 positions. 

The unit test `assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]` confirms that the function works correctly. 
```python
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
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
```  ```