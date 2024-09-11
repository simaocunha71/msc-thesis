```
def find_tuples(lst, k):
    result = []
    for tuple in lst:
        if all(i % k == 0 for i in tuple):
            result.append(tuple)
    return result
```

Explanation:
This solution defines a function called `find_tuples` that takes in two parameters: a list of tuples called `lst` and an integer called `k`. The function initializes an empty list called `result` to store the tuples that satisfy the condition. 

The function then iterates over each tuple in the `lst` using a for loop. Inside the loop, it uses a list comprehension and the `all()` function to check if all the elements in the tuple are divisible by `k`. The `all()` function returns `True` if all the elements in an iterable (in this case, the tuple) satisfy the condition, and `False` otherwise. If all the elements in the tuple are divisible by `k`, the tuple is appended to the `result` list. 

Finally, the function returns the `result` list, which contains all the tuples that satisfy the condition. 

The provided assert statement is used to test the function and ensures that it returns the expected result when given the input `[(6, 24, 12), (7, 9, 6), (12, 18, 21)]` and `6`. 

The function can be used to find all the tuples in a given list that have all their elements divisible by a specified integer.

```python
find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6)
```

This will return `[(6, 24, 12)]`, which is the only tuple in the input list where all the elements are divisible by 6.

```python
find_tuples([(2, 4, 6), (7, 9, 11), (12, 18, 21)], 3)
```

This will return `[(2, 4, 6)]`, as it is the only