The problem is asking to count the number of non-empty substrings of a given string. For example, if the given string is "abc", the non-empty substrings are "a", "ab", "abc", "b", "bc", "c", and the total count is 6.

Here is the Python function to solve this problem:

```
def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] != "":
                count += 1
    return count
```

This function uses two nested loops to generate all possible substrings of the given string. For each substring, it checks if the substring is not empty and increments the count if it's not. Finally, it returns the total count of non-empty substrings. 

The unit test `assert number_of_substrings("abc") == 6` ensures that the function is working correctly. 

For example, if the input string is "abc", the function will generate the following substrings: "a", "ab", "abc", "b", "bc", "c", and the total count is 6, which is the expected output. 

Note that the time complexity of this function is O(n^2) due to the nested loops, where n is the length of the input string. If the input string is very large, this function may take a long time to execute. 