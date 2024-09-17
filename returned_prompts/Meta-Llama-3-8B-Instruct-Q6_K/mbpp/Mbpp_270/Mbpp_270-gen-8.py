```
def sum_even_and_even_index(lst):
    return sum(num for i, num in enumerate(lst) if i % 2 == 0 and num % 2 == 0)
```


This function works by using a generator expression to iterate over the list and its indices. The `enumerate` function is used to get both the index and the value of each element in the list. The `if` condition checks if the index is even (i % 2 == 0) and if the value is even (num % 2 == 0). The `sum` function is then used to add up all the values that meet these conditions. The unit test `assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30` ensures that this function is working correctly. 