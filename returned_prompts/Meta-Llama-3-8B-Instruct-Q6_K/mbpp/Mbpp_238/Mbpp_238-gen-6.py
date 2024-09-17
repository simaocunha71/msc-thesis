You can use a loop to count the number of non-empty substrings of a given string. Here is a Python function that does this:

```
def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            count += 1
    return count
```

This function works by iterating over each character in the string, and for each character, it iterates over all the characters to the right of it. This effectively counts all the non-empty substrings of the string. For example, for the string "abc", the function would count the substrings "a", "ab", "abc", "b", "bc", and "c", resulting in a total of 6 substrings. 

However, this function is not very efficient, as it has a time complexity of O(n^2), where n is the length of the string. A more efficient solution would be to use the formula for the number of non-empty substrings of a string of length n, which is n*(n+1)/2. Here is a Python function that uses this formula:

```
def number_of_substrings(s):
    return len(s) * (len(s) + 1) // 2
```

This function is much more efficient, as it has a time complexity of O(1). It simply calculates the number of non-empty substrings of the string using the formula, and returns this value. This function would return 6 for the string "abc", as expected. 