```
def find_tuples(lst, k):
    return [tuple(x for x in t if x % k == 0) for t in lst if all(x % k == 0 for x in t)]
```

Explanation:

The function `find_tuples` takes a list of tuples and an integer `k` as input. It uses a list comprehension to iterate over each tuple in the list, and another list comprehension inside it to select only the elements in the tuple that are divisible by `k`. The `all` function is used to check if all the elements in the tuple are divisible by `k`. If they are, the tuple is returned as part of the result list.

The `find_tuples` function returns a list of tuples, where each tuple contains only the elements that are divisible by `k`. This is achieved by using a conditional expression (`if`) inside the list comprehension to filter out the elements that are not divisible by `k`.

For example, if we call `find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6)`, it will return `[(6, 24, 12)]`. This is because the first tuple `(6, 24, 12)` is the only tuple in the list where all the elements are divisible by `6`.

This solution uses the `all` function to check if all the elements in a tuple are divisible by `k`. The `all` function returns `True` if all elements in an iterable are true (or if the iterable is empty). In this case, it is used to check if all the elements in the tuple are divisible by `k`.

Overall, this solution effectively finds and returns the tuples that have all elements divisible by `k` from the given list of tuples.

"""
```python
def find_tuples(lst, k):
    return [tuple(x for x in t if x % k == 0) for t in lst if all(x % k == 0 for x in t)]
```

Explanation:
The function `find_tuples`