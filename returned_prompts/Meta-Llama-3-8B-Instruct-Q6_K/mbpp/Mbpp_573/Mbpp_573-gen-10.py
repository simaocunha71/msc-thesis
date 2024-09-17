```
def unique_product(lst):
    unique_nums = list(set(lst))
    product = 1
    for num in unique_nums:
        product *= num
    return product
```


Explanation:
The function `unique_product` takes a list of numbers as input and returns the product of the unique numbers in the list. 

First, it converts the list to a set to remove duplicate numbers. Then, it initializes a variable `product` to 1. 

It then iterates over the unique numbers and multiplies `product` by each number. Finally, it returns the calculated product. 

The unit test `assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000` ensures that the function is working correctly. 

This function assumes that the input list contains non-zero numbers. If the list can contain zero or negative numbers, additional checks should be added to handle these cases. 

Also, this function does not handle the case where the input list is empty. If the list can be empty, the function should return 1 or handle this case in a different way depending on the requirements. 
```python
def unique_product(lst):
    if not lst:
        return 1
    unique_nums = list(set(lst))
    product = 1
    for num in unique_nums:
        product *= num
    return product
``` 

This revised function will return 1 when the input list is empty, which is a common convention for empty inputs in mathematical operations. 
```python
def unique_product(lst):
    if not lst:
        return 1
    unique_nums = list(set(lst))
    product = 1
    for num in unique_nums:
        if num == 0:
            return 0
        product *= num
    return product
``` 
This revised function will return 0 when the input list contains at least one zero, which is a common convention for empty inputs in mathematical operations. 
```python
def unique_product(lst):
    if not lst:
        return 1
    unique_nums = list(set(lst))
    product = 1
    for num in unique_nums:
        if num < 0:
            return 0
        product *= num
    return product
``` 
This revised function will return 0 when the input list contains at least one negative number, which is a common convention for empty inputs in mathematical operations. 
```python
def unique