```
def next_smallest_palindrome(n):
    n += 1
    while not is_palindrome(str(n)):
        n += 1
    return n

def is_palindrome(s):
    return s == s[::-1]
```
The function `next_smallest_palindrome` starts by incrementing the input number `n` by 1. Then it enters a loop where it checks if the string representation of `n` is a palindrome. If it's not, it increments `n` by 1 and checks again. This process continues until `n` becomes a palindrome. Finally, the function returns the smallest palindrome found.

The helper function `is_palindrome` checks if a given string is a palindrome by comparing it with its reverse. If they are the same, the string is a palindrome. This function is used in the main function to check if a number is a palindrome.