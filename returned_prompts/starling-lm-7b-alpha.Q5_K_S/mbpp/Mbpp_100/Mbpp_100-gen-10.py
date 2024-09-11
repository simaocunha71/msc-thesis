```
def next_smallest_palindrome(n):
    def is_palindrome(m):
        s = str(m)
        return s == s[::-1]

    while True:
        n += 1
        if is_palindrome(n):
            return n
```

In this code, the function `next_smallest_palindrome` takes an integer `n` as an input and returns the next smallest palindrome of this integer as an integer. To achieve this, a helper function `is_palindrome` is defined to check whether a given number is a palindrome.

The `is_palindrome` function takes an integer `m` as input and converts it to a string `s`. It then checks if the string `s` is equal to its reverse `s[::-1]`. If they are equal, it means that `m` is a palindrome, and the function returns `True`. Otherwise, it returns `False`.

In the `next_smallest_palindrome` function, a `while` loop is used to increment the value of `n` by 1 until a palindrome is found. Once a palindrome is found, it is returned as the result.

To test the `next_smallest_palindrome` function, an assertion is made that it should return `101` when given the input `99`. This assertion serves as a test case to verify the correctness of the function.

Overall, this code provides a solution to find the next smallest palindrome of a given integer using a helper function to check if a number is a palindrome.

```python
def next_smallest_palindrome(n):
    def is_palindrome(m):
        s = str(m)
        return s == s[::-1]

    while True:
        n += 1
        if is_palindrome(n):
            return n
```

This solution utilizes a helper function called `is_palindrome` to determine if a number is a palindrome. The `is_palindrome` function converts the input number to a string and checks if the string is equal to its reverse. If