```
def sum_even_and_even_index(lst):
    return sum(num for i, num in enumerate(lst) if i % 2 == 0 and num % 2 == 0)
```


Explanation:
This function uses the built-in `enumerate` function to iterate over the list and get both the index and the value of each element. The condition `i % 2 == 0` checks if the index is even, and `num % 2 == 0` checks if the value is even. The `sum` function is used to add up the even numbers at even positions. The unit test `assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30` ensures the function works correctly.