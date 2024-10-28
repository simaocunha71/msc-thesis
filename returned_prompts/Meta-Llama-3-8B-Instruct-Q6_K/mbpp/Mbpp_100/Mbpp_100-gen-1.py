```
def next_smallest_palindrome(n):
    n += 1
    while not is_palindrome(str(n)):
        n += 1
    return n

def is_palindrome(s):
    return s == s[::-1]
```    
The function `next_smallest_palindrome(n)` finds the next smallest palindrome after the given integer `n`. It does this by incrementing `n` until a palindrome is found. The helper function `is_palindrome(s)` checks if a string `s` is a palindrome by comparing it with its reverse. The `next_smallest_palindrome` function uses this helper function to find the next smallest palindrome.

The unit test `assert next_smallest_palindrome(99)==101` ensures that the function works correctly. It checks that the next smallest palindrome after 99 is 101. If the function is implemented correctly, this test will pass. If not, it will raise an AssertionError.