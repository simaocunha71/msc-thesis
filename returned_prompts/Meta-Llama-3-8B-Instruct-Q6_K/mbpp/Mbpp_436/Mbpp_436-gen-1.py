```
def neg_nos(lst):
    return [x for x in lst if x < 0]
```
This function uses a list comprehension to iterate over the input list `lst` and includes only the numbers that are less than 0 (i.e., the negative numbers). The result is a new list containing only the negative numbers from the original list. For example, if the input is `[-1,4,5,-6]`, the output will be `[-1,-6]`. The unit test `assert neg_nos([-1,4,5,-6]) == [-1,-6]` confirms this behavior. 