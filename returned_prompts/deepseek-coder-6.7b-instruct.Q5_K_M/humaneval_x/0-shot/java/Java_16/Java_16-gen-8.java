        Set<Character> distinctChars = new HashSet<>();
        for (int i = 0; i < string.length(); i++) {
            distinctChars.add(Character.toLowerCase(string.charAt(i)));
        }
        return distinctChars.size();
    }
}


A: Here is a Python solution for your question:

```python
def count_distinct_characters(string):
    # Convert string to lower case and remove duplicate characters using set
    return len(set(string.lower()))
```

This code converts the input string to lower case and then uses a set to remove any duplicate characters. The length of the set is the number of distinct characters in the string.

Test the function:

```python
print(count_distinct_characters("xyzXYZ"))  # Output: 3
print(count_distinct_characters("Jerry"))  # Output: 4
```

This code works by iterating over each character in the string, converting it to lower case, and adding it to a set. A set in Python is a data structure that only contains unique elements. Therefore, any duplicate characters in the string will be removed when it is converted to a set. Finally, the length of the set is returned as the number of distinct characters in the string.

Note: The order of characters in the string is not considered in this solution.

Hope this helps to solve your problem in Python.

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```