```
def round_and_sum(lst):
    rounded_nums = [round(num) for num in lst]
    total_sum = sum(rounded_nums)
    return total_sum * len(lst)
```



The task is to create a function that takes a list of numbers as input, rounds each number to the nearest integer, and then calculates the total sum of the rounded numbers. The function should return the total sum multiplied by the length of the list.

The provided unit test `assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243` helps to understand the problem better.

Here is the solution:

```
def round_and_sum(lst):
    rounded_nums = [round(num) for num in lst]
    total_sum = sum(rounded_nums)
    return total_sum * len(lst)
```

This function uses a list comprehension to round each number in the input list to the nearest integer. It then calculates the total sum of the rounded numbers using the built-in `sum` function. Finally, it returns the total sum multiplied by the length of the list.