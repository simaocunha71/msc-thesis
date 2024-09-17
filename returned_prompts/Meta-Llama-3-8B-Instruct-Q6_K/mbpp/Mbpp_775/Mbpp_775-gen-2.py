```
def odd_position(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True
```
The function `odd_position` takes a list as an input and checks whether every odd index contains an odd number. It iterates over the list with a step of 2, starting from the second element (index 1). For each element at an odd index, it checks if the element is odd (i.e., if the remainder of the division of the element by 2 is 1). If it finds an even number at an odd index, it immediately returns `False`. If it checks all elements at odd indices and doesn't find any even numbers, it returns `True`. 

This function passes the given unit test `assert odd_position([2,1,4,3,6,7,6,3]) == True`.  It also passes other similar test cases, for example, `assert odd_position([1,3,5,7]) == True` and `assert odd_position([2,4,6,8]) == False`. 

However, the function will return `False` for the test case `assert odd_position([1]) == True` because the function is designed to return `False` for lists with less than two elements. To fix this, we can add a condition to return `True` for lists with less than two elements. Here is the updated function:

```
def odd_position(lst):
    if len(lst) < 2:
        return True
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True
```  Now the function should pass all the given test cases.  It will return `True` for lists with less than two elements and `False` for lists with two or more elements that contain even numbers at odd indices.  