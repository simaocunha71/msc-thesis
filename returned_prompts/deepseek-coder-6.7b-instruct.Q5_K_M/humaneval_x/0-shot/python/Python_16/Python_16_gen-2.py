
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This function works by converting the string to lowercase and then converting it to a set. A set in Python is a collection of unique elements, so this will remove any duplicate characters. The function then returns the length of the set, which is the number of unique characters in the string.

```python
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
```

These assertions will check that the function is working correctly. If the function is correct, these assertions should pass without throwing an error.
</p></details>

## 5. Write a Python function that calculates the sum of the squares of all the digits of a number.

<details><summary>Click to expand</summary><p>

