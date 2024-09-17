```
def neg_nos(lst):
    return [i for i in lst if i < 0]
```
This function uses a list comprehension to iterate over the input list `lst` and returns a new list containing only the elements that are less than 0, i.e., the negative numbers.

The unit test `assert neg_nos([-1,4,5,-6]) == [-1,-6]` ensures that the function works correctly. It checks if the output of the function is `[-1,-6]` when the input is `[-1,4,5,-6]`. If the output is not `[-1,-6]`, the test fails. In this case, the output is indeed `[-1,-6]`, so the test passes.