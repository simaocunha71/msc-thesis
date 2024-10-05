

```python
def same_chars(s0: str, s1: str) -> bool:
    return sorted(s0) == sorted(s1)
```

Explanation:

The function `same_chars` takes two strings `s0` and `s1` as input. It returns `True` if the two strings contain the same characters, and `False` otherwise. 

It does this by sorting each string and then comparing the sorted strings. If the sorted strings are equal, that means the two original strings have the same characters (in the same quantities, of course). If the sorted strings are not equal, that means the two original strings do not have the same characters.

Here is the test:

```python
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
print(same_chars('abcd', 'dddddddabc'))  # True
print(same_chars('dddddddabc', 'abcd'))  # True
print(same_chars('eabcd', 'dddddddabc'))  # False
print(same_chars('abcd', 'dddddddabce'))  # False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # False
```

This solution has a time complexity of O(n log n) because of the sorting operation. The space complexity is O(n) because of the space needed to store the sorted strings.
"""

# ---------------------
# SOLUTION 2
# ---------------------

"""
