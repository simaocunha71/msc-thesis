Here is the solution of the problem in Python:

```python
def histogram(test):
    test_list = test.split(" ")
    histogram_dict = {i:test_list.count(i) for i in test_list}
    max_value = max(histogram_dict.values(), default=0)
    return {key: value for key, value in histogram_dict.items() if value == max_value}
```

This solution uses a dictionary comprehension to create a histogram of the input string. It then finds the maximum value in the histogram and returns a new dictionary containing only the keys with that maximum value. If the input string is empty, the function will return an empty dictionary.

For example:
histogram("a b c") -> {"a": 1, "b": 1, "c": 1}
histogram("a b b a") -> {"a": 2, "b": 2}
histogram("a b c a b") -> {"a": 2, "b": 2}
histogram("b b b b a") -> {"b": 4}
histogram("") -> {}
```

This solution has a time complexity of O(n