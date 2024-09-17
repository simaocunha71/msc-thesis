```
def sum_even_and_even_index(lst):
    sum_even = 0
    for i, num in enumerate(lst):
        if i % 2 == 0 and num % 2 == 0:
            sum_even += num
    return sum_even
```


Explanation:
The function `sum_even_and_even_index` takes a list of numbers as input. It initializes a variable `sum_even` to zero. Then, it iterates over the list using the `enumerate` function, which returns both the index and the value of each element. For each element, it checks if the index is even (using the condition `i % 2 == 0`) and if the number is even (using the condition `num % 2 == 0`). If both conditions are true, it adds the number to the `sum_even` variable. Finally, it returns the `sum_even` variable.

The unit test `assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30` ensures that the function works correctly. The function correctly sums the even numbers at even positions (6, 12, 18) in the list and returns 30.