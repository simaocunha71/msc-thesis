```
def count_distinct_characters(string: str) -> int:
    string = string.lower()  # convert to lowercase for case-insensitive counting
    return len(set(string))  # use set to remove duplicates and get the length
```


This function takes a string as input and returns the number of distinct characters in the string, ignoring case. The `set` function is used to remove duplicates from the string, and then the length of the set is returned. The `lower` function is used to convert the string to lowercase, so that 'a' and 'A' are considered the same character. This allows the function to correctly count distinct characters regardless of case.