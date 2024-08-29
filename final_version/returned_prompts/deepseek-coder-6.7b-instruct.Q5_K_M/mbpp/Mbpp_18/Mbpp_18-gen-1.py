Here is a Python solution using list comprehension:

```python
def remove_dirty_chars(s1, s2):
    return ''.join([char for char in s1 if char not in s2])
```

Here, we iterate over each character in the first string and only keep it if it does not exist in the second string. The `join` function is used to concatenate the characters back into a string.

Test the function:

```python
print(remove_dirty_chars("probasscurve", "pros"))  # Output: 'bacuve'
```

In the above function, the characters 'b', 'a', 's', 'c', 'u', 'v', 'e' are removed from the string 'probasscurve' as they exist in the string 'pros'.

The time complexity of this function is O(n*m) where n is the length of the first string and m is the length of the second string.

This function assumes that the characters in the second string are unique. If the characters in the second string are not unique, then we need to count the occurrences of characters in the second string and remove the minimum count from the first string.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
"""
