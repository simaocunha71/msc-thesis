```
def round_and_sum(lst):
    lst = [round(num) for num in lst]
    return sum(lst) * len(lst)
```


In this solution, the function `round_and_sum` takes a list of numbers as input, rounds each number to the nearest integer using a list comprehension, and then calculates the total sum of the rounded numbers using the built-in `sum` function. Finally, it returns the product of the total sum and the length of the list. The unit test `assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243` ensures that the function works correctly.