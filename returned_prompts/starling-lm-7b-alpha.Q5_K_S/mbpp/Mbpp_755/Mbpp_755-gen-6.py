Here is a Python program to solve this problem:

```python
def second_smallest(nums):
    smallest = min(nums)
    second_smallest = min(x for x in nums if x != smallest)
    return second_smallest
```

Explanation:
In this solution, we first find the smallest number in the list using the `min()` function. Then, we use a generator expression to find the second smallest number, excluding the smallest number from consideration using the `if x != smallest` condition. Finally, we return the second smallest number.

The `assert second_smallest([1, 2, -8, -2, 0, -2])==-2` statement is a way to test the correctness of the `second_smallest` function. It checks if the `second_smallest` function correctly returns -2 when given the list `[1, 2, -8, -2, 0, -2]`. If the assertion is true, it means that the function is working correctly.

Overall, this solution efficiently finds the second smallest number in a given list and passes the test case provided.






































































































```

```



```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```