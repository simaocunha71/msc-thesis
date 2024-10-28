```
def sum_even_and_even_index(lst):
    return sum(x for x in lst[::2] if x % 2 == 0)
```


Explanation:
The function `sum_even_and_even_index` takes a list as input and returns the sum of even numbers at even positions. 

The expression `lst[::2]` is used to get the elements at even positions. The `::2` is a slice that starts at the beginning, goes to the end, and steps by 2.

The expression `x for x in lst[::2] if x % 2 == 0` is a generator expression that filters the even numbers from the list and sums them up. The `if x % 2 == 0` part filters the even numbers, and the `sum` function adds them up.

The unit test `assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30` ensures that the function returns the correct sum for the given input. 

This function works by iterating over the list and summing up the even numbers at even positions. It does not require a separate function to check if the index is even, as the slice operation achieves this automatically. 