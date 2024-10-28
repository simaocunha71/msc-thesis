

def count_distinct_characters(string: str) -> int:
    from collections import Counter
    return len(Counter(string.lower()))




# Test Cases:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4




# Explanation:
# This function uses the Counter class from the collections module to count the occurrences of each character in the string. By converting the string to lowercase, we ensure that uppercase and lowercase versions of the same character are counted as a single character. The length of the Counter object gives us the number of distinct characters in the string, which is then returned.

```python
from collections import Counter

def count_distinct_characters(string: str) -> int:
    return len(Counter(string.lower()))
```

In the provided test cases, 'xyzXYZ' consists of 3 distinct characters ('x', 'y', 'z'), and 'Jerry' consists of 4 distinct characters ('j', 'e', 'r', 'y'). The function correctly counts the distinct characters in both cases and returns the result.

```python
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

By using the Counter class and converting the string to lowercase, the function efficiently counts the distinct characters in the string regardless of case.
```python

```
```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

``