```
def count_distinct_characters(string: str) -> int:
    return len(set(string.casefold()))
```


This function works by first converting the input string to a set, which removes any duplicate characters. The `casefold()` method is used to make the function case-insensitive, so that characters are considered distinct regardless of whether they are uppercase or lowercase. The `len()` function is then used to count the number of elements in the set, which is the number of distinct characters in the string.