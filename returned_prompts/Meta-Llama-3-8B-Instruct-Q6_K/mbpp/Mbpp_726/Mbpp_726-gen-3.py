```
def multiply_elements(t):
    result = ()
    for i in range(len(t) - 1):
        result += (t[i] * t[i+1],)
    return result
```


In this function, we create an empty tuple `result` and then iterate over the input tuple `t` (excluding the last element). For each element `t[i]`, we multiply it with the next element `t[i+1]` and add the result to the `result` tuple. Finally, we return the `result` tuple. The unit test `assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)` ensures that the function works correctly. 