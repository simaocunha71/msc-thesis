```
def sum_squares(lst):
    return round(sum([math.ceil(i) ** 2 for i in lst]))
```

Explanation:
The function `sum_squares` takes a list of numbers as input. It uses a list comprehension to square each number in the list, rounds each number to the upper integer using `math.ceil`, and then sums the results. The `math.ceil` function is used to round each number to the upper integer, and the `**` operator is used to square each number. The `sum` function is used to calculate the sum of the squared numbers. The result is then rounded using the `round` function.