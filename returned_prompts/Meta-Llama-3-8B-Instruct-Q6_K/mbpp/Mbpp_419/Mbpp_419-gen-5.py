```
def round_and_sum(lst):
    rounded_sum = sum(round(num) for num in lst)
    return rounded_sum * len(lst)
```


The unit test provided is `assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243`, which means the function should round every number in the list and then print the total sum multiplied by the length of the list. 

The function `round_and_sum` takes a list of numbers as input, rounds each number using a generator expression, calculates the total sum using the built-in `sum` function, and then returns the total sum multiplied by the length of the list. 

This function will work correctly for any list of numbers and will pass the provided unit test. 