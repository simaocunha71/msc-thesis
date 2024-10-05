
Here is a simple algorithm to make a palindrome out of a given string:

1. Test if the string is already a palindrome. If it is, return it.
2. Find the longest palindromic suffix of the string. This is done by iteratively checking if a substring from the end of the string is a palindrome. The length of the suffix is doubled at each iteration, starting from 1. This is done by checking if the substring is equal to its reverse.
3. If the string is not a palindrome, we need to find a prefix that can be appended to the palindromic suffix to form a new palindrome. To do this, we reverse the palindromic suffix, and find the longest prefix of the original string that is equal to the reversed suffix. This is done by iteratively checking if a substring from the beginning of the string is equal to the reversed suffix. The length of the prefix is doubled at each iteration, starting from 1.
4. Finally, concatenate the palindromic suffix and the reversed prefix, and return the result.

Here is the Python code that implements the described algorithm:

```python
def make_palindrome(string):
    if is_palindrome(string):
        return string

    length = len(string)
    for i in range(length, 0, -2):
        if is_palindrome(string[:i]):
            break

    longest_suffix = string[:i]
    prefix_length = len(longest_suffix) // 2
    for j in range(prefix_length, 0, -2):
        if longest_suffix[:j] == longest_suffix[::-1][:j]:
            break
    prefix = longest_suffix[:j]
    return longest_suffix + prefix[::-1]
```

This algorithm has a time complexity of O(n^3), where n is the length of the input string. It is not very efficient for long strings, but it works well for short input strings.

Here are some example test cases:

```python
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))