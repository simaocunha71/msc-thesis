```
def neg_nos(lst):
    return [x for x in lst if x < 0]
```


Explanation:
The problem is asking to write a function that takes a list of numbers as input and returns a new list containing only the negative numbers from the original list.

The unit test provided is `assert neg_nos([-1,4,5,-6]) == [-1,-6]`, which means the function should return a list of negative numbers from the given list.

The solution uses a list comprehension to iterate over the input list `lst` and include only the numbers that are less than 0 (i.e., the negative numbers) in the output list.

The function is defined as `def neg_nos(lst):` and the list comprehension is `[x for x in lst if x < 0]`. The `if x < 0` condition filters out the non-negative numbers, leaving only the negative numbers in the output list.

For example, if the input list is `[-1,4,5,-6]`, the function will return `[-1,-6]`, which is the expected output.