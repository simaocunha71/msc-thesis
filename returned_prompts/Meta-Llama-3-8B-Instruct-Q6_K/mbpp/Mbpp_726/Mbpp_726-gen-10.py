```
def multiply_elements(t):
    result = ()
    for i in range(len(t) - 1):
        result += (t[i] * t[i+1],)
    return result
```


This function iterates over the input tuple, multiplying each element with the next one, and adds the results to a new tuple. The result is then returned. The unit test `assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)` ensures that the function works correctly. 

Note: The unit test provided in the question does not include the last element of the tuple in the expected result. This is because the last element of the tuple does not have a next element to multiply with, so it is not included in the result. 

Also, the problem statement does not specify what to do with the last element of the tuple, but based on the unit test, it seems that the last element is not included in the result. 

If you want to include the last element in the result, you can modify the function to do so. For example:
```
def multiply_elements(t):
    result = ()
    for i in range(len(t)):
        if i < len(t) - 1:
            result += (t[i] * t[i+1],)
        else:
            result += (t[i],)
    return result
```
This modified function includes the last element in the result. 

However, please note that the original problem statement does not specify what to do with the last element, so this modification may not be consistent with the original problem. 

In any case, the original function provided in the answer is consistent with the unit test provided, and it does not include the last element in the result. 