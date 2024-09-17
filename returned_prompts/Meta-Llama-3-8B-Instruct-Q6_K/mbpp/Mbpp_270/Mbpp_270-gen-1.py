```
def sum_even_and_even_index(lst):
    return sum(num for i, num in enumerate(lst) if i % 2 == 0 and num % 2 == 0)
```


Explanation:
The problem is asking to create a function that takes a list as input and returns the sum of all even numbers that are at even positions in the list.

The unit test `assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30` helps in understanding the problem better. It shows that the function should return the sum of even numbers at even positions in the list.

The solution uses a generator expression to iterate over the list with the `enumerate` function, which returns both the index and the value of each element in the list. The condition `i % 2 == 0` checks if the index is even, and the condition `num % 2 == 0` checks if the number is even. The `sum` function is then used to add up all the numbers that meet both conditions.