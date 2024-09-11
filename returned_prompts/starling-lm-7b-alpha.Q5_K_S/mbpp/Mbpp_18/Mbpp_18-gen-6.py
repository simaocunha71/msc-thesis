"""
This can be achieved in python using list comprehension and the built-in functions in Python. Here is a step by step guide on how to do it:

1. Convert the second string into a set to make lookup faster. This is because set operations in Python are faster than list operations. Here's how you do it:

   second_string = set("pros")

2. Iterate over the first string and check if the character is present in the second string. If it is not, add it to a new string. Here's how you can do it:

   result = ''.join(ch for ch in original_string if ch not in second_string)

The final code would be:

def remove_dirty_chars(original_string, dirty_chars):
    second_string = set(dirty_chars)
    result = ''.join(ch for ch in original_string if ch not in second_string)
    return result
"""

from collections import defaultdict

def remove_dirty_chars(s1, s2):
    d = defaultdict(int)
    for i in range(len(s2)):
        d[s2[i]] += 1

    s3 = ''
    for i in range(len(s1)):
        if d[s1[i]] == 0:
            s3 += s1[i]
    return s3


# Driver code
s1 = "probasscurve"
s2 = "pros"
print(remove_dirty_chars(s1, s2))

# This code is contributed by 29AjayKumar
```
```

```
```

```python

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
```
```
