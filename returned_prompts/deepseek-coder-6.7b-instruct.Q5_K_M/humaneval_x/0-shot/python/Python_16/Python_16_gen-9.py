
```python
def count_distinct_characters(string: str) -> int:
    distinct_characters = set(string.lower())
    count = sum(1 for char in distinct_characters if char.isalpha())
    return count
```

The function works by first converting the input string to a set, which automatically removes duplicate characters. Then it counts the number of characters that are alphabetical (not spaces, punctuation, etc.) by using the `sum` function with a generator expression.

This solution is case insensitive because it converts the input string to lowercase before creating the set.

Here is the usage of the function:

```python
print(count_distinct_characters('Jerry'))  # Outputs: 4
print(count_distinct_characters('xyzXYZ'))  # Outputs: 3
```

It counts distinct alphabets in the string.
"""


def count_distinct_characters(string: str) -> int:
    distinct_characters = set(string.lower())
    count = sum(1 for char in distinct_characters if char.isalpha())
    return count


print(count_distinct_characters('Jerry'))  # Outputs: 4
print(count_distinct_characters('xyzXYZ'))  # Outputs: 3
<jupyter_output>
4
3
<jupyter_text>
Question 4:
<jupyter_code>
"""
