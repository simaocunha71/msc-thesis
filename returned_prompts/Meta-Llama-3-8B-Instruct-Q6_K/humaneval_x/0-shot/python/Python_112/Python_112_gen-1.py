```
def reverse_delete(s,c):
    result = ''.join([i for i in s if i not in c])
    return result, result == result[::-1]
```



Explanation:

*   First, we create a new string `result` by iterating over each character `i` in the string `s` and checking if `i` is not in the string `c`. If it's not, we add it to the `result` string.
*   Then, we return a tuple containing the `result` string and a boolean value indicating whether the `result` string is a palindrome or not. We check if the `result` string is equal to its reverse (`result[::-1]`) and return `True` if it is, and `False` otherwise.

This solution works by creating a new string that excludes all characters from `s` that are also in `c`, and then checking if the resulting string is a palindrome. The `join` method is used to concatenate the characters in the new string, and the `[::-1]` slice notation is used to get the reverse of the string. The `==` operator is used to check if the string is equal to its reverse. If it is, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`.