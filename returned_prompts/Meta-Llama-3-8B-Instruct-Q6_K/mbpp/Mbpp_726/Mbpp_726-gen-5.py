```
def multiply_elements(t):
    result = ()
    for i in range(len(t)-1):
        result += (t[i] * t[i+1],)
    return result
```


The function `multiply_elements` takes a tuple `t` as input and returns a new tuple where each element is the product of the corresponding elements in `t` and `t` shifted by one position. The function uses a for loop to iterate over the elements of `t` (excluding the last one), multiplies each element with the next one, and adds the result to the `result` tuple.

The unit test `assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)` ensures that the function works correctly for the given input. If the function returns a different result, the test will fail.

The function can be used as follows:
```
result = multiply_elements((1, 5, 7, 8, 10))
print(result)  # Output: (5, 35, 56, 80)
```


Note: The function does not handle the case where the input tuple has only one element. In this case, it would be more natural to return an empty tuple or raise an exception. However, the problem statement does not specify what to do in this case, so the function does not handle it. If you want to handle this case, you can add a simple check at the beginning of the function:
```
if len(t) == 1:
    return ()
```


This would return an empty tuple if the input has only one element. You can adjust this behavior according to your needs.