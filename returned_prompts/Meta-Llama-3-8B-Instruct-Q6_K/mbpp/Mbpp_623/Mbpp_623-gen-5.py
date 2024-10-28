```
def nth_nums(lst, n):
    return [i ** n for i in lst]
```
This function uses a list comprehension to compute the n-th power of each number in the input list `lst`. The result is a new list containing the n-th powers of the original numbers.

The unit test `assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` ensures that the function works correctly for the given input and expected output.