```
def nth_nums(lst, n):
    return [i**n for i in lst]
```



The provided unit test `assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` suggests that the function should compute the n-th power of each number in the list. 

Here, we can use list comprehension to achieve this. The function `nth_nums(lst, n)` takes a list `lst` and an integer `n` as input, and returns a new list where each element is the nth power of the corresponding element in the input list. 

For example, if we call `nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)`, it will return `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`, which are the squares of the numbers from 1 to 10. 

The function uses the expression `i**n` to compute the n-th power of each number `i` in the list, and the list comprehension `[i**n for i in lst]` to create the new list with the results. 

This function assumes that the input list contains only numbers, and that the input integer `n` is non-negative. If the input list contains non-numeric values, or if `n` is negative, the function may raise an error or produce unexpected results. 

However, the unit test provided suggests that the function should work correctly for the given inputs, so we can assume that the input list contains only numbers and that `n` is non-negative. 

In this case, the function can be implemented as follows:
```
def nth_nums(lst, n):
    return [i**n for i in lst]
``` 