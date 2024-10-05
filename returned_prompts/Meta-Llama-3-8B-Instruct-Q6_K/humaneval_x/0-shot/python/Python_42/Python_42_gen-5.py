```
def incr_list(l: list):
    return [i+1 for i in l]
```
This function uses a list comprehension to create a new list where each element is the original element incremented by 1. The `i+1` expression is evaluated for each element `i` in the original list, and the results are collected into a new list. The function takes a list `l` as input and returns the incremented list.