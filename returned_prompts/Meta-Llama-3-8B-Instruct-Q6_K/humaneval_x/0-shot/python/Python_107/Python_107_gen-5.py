```
def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return even_count, odd_count
```



Explanation:

*   The function `even_odd_palindrome` takes an integer `n` as input and returns a tuple containing the number of even and odd integer palindromes within the range(1, n), inclusive.
*   The function initializes two counters, `even_count` and `odd_count`, to keep track of the number of even and odd integer palindromes, respectively.
*   It then iterates over the range(1, n + 1) using a for loop.
*   For each integer `i` in the range, it checks if the integer is a palindrome by converting it to a string and comparing it with its reverse.
*   If the integer is a palindrome, it checks if it's even or odd using the modulo operator `%`. If it's even, it increments the `even_count` counter; otherwise, it increments the `odd_count` counter.
*   Finally, the function returns a tuple containing the `even_count` and `odd_count` values.

Example:

```
>>> even_odd_palindrome(12)
(4, 6)
```

In this example, the function returns a tuple `(4, 6)`, indicating that there are 4 even integer palindromes (2, 4, 6, 8) and 6 odd integer palindromes (1, 3, 5, 7, 9, 11) within the range(1, 12), inclusive.