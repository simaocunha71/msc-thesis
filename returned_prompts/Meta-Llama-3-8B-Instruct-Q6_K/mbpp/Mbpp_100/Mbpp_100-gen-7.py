```
def next_smallest_palindrome(n):
    n += 1
    while not is_palindrome(str(n)):
        n += 1
    return n

def is_palindrome(s):
    return s == s[::-1]
```    
The function `next_smallest_palindrome(n)` takes an integer `n` as input, increments it by 1, and then checks if the resulting number is a palindrome using the helper function `is_palindrome(s)`. If the number is not a palindrome, it increments the number again and checks again until it finds a palindrome. The function then returns the next smallest palindrome. The `is_palindrome(s)` function checks if a string `s` is a palindrome by comparing it with its reverse. The unit test `assert next_smallest_palindrome(99)==101` ensures that the function works correctly.    



