    for char in c:
        s = s.replace(char, '')
    
    return (s, s == s[::-1])

I have tried to solve these questions but I am unable to solve the last one. The code for this question is given below.
def reverse_delete(s,c):
    for char in c:
        s = s.replace(char, '')

    return (s, s == s[::-1])

Can anyone help me to solve this question?

A: The problem with your code is that s == s[::-1] is checking whether the string is the same forwards and backwards. This will not work correctly for strings that have been manipulated by the replace method.
Here is the corrected code:
def reverse_delete(s,c):
    for char in c:
        s = s.replace(char, '')

    # reverse the string and remove the characters that were also deleted
    reverse_s = s[::-1]
    for char in c:
        reverse_s = reverse_s.replace(char, '')

    # The string is a palindrome if it is the same forwards and backwards
    is_palindrome = s == s[::-1]

    return (reverse_s[::-1], is_palindrome)

This code first removes the characters in c from s, then reverses the string and removes the characters in c. The string is then checked to see if it is the same forwards and backwards (i.e., if it is a palindrome). The result is then returned as a tuple with the reversed string and the palindrome check.

A: The problem is that you are reversing the string before removing the characters in c, which means that the characters you are trying to remove are no longer in their original positions.
Here is the corrected version of your code:

```python
def reverse_delete(s,c):
    for char in c:
        s = s.replace(char, '')
    reverse_s = s[::-1]
    for char in c:
        reverse_s = reverse_s.replace(char, '')
    is_palindrome = reverse_s == reverse