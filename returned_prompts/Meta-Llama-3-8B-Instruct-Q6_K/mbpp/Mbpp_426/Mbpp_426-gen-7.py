```
def filter_oddnumbers(lst):
    return [num for num in lst if num % 2 != 0]
```
This function uses a list comprehension to iterate over the input list `lst` and includes only the numbers that are odd (i.e., the remainder when divided by 2 is not 0). The result is a new list containing only the odd numbers from the original list. 

For example, if the input list is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, the function will return `[1, 3, 5, 7, 9]`. 

This function passes the given unit test. 

Note: The unit test is `assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]`. This test checks if the function returns the expected result when given the input list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. The expected result is `[1, 3, 5, 7, 9]`, which is the list of odd numbers from the input list. The function passes this test if it returns the expected result. 

The function can be used as follows:
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter_oddnumbers(numbers)
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]
``` 
This code defines a list `numbers` containing the numbers from 1 to 10, then calls the `filter_oddnumbers` function with this list as input, and finally prints the result. The output will be the list of odd numbers from the input list.  ```python
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