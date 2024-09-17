The problem is asking to count the number of non-empty substrings of a given string. For example, if the string is "abc", the non-empty substrings are "a", "ab", "abc", "b", "bc", "c". Therefore, the output should be 6.

Here is a Python function that solves this problem:
```
def number_of_substrings(s):
    return len(s) * (len(s) + 1) // 2
```
This function works by using the formula for the sum of an arithmetic series. The number of non-empty substrings of a string of length n is equal to the sum of the first n natural numbers, which is n*(n+1)//2. This function takes a string s as input and returns the number of non-empty substrings of s. The unit test `assert number_of_substrings("abc") == 6` passes with this function.