You can solve this problem by using a loop to generate all possible substrings of the given string, and then count the non-empty ones. Here is a Python function that does this:

```
def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring:
                count += 1
    return count
```

This function works by iterating over all possible start indices `i` and end indices `j` of the substrings. It then constructs the substring `s[i:j]` and increments the count if the substring is not empty. The function returns the total count of non-empty substrings.

The unit test `assert number_of_substrings("abc") == 6` ensures that the function returns the correct count for the string "abc". The function should return 6 because the non-empty substrings of "abc" are "a", "ab", "abc", "b", "bc", and "c". 

Note that this function has a time complexity of O(n^2) because it generates all possible substrings, where n is the length of the input string. If the input string is very long, this function may be slow. However, it is simple and easy to understand. If you need a more efficient solution, you may want to consider using a different approach. 