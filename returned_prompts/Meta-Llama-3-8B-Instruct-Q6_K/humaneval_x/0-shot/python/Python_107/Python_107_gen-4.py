```
def even_odd_palindrome(n):
    even_palindromes = 0
    odd_palindromes = 0

    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_palindromes += 1
            else:
                odd_palindromes += 1

    return even_palindromes, odd_palindromes
```



Here is a Python solution that checks for each number in the range 1 to n if it is a palindrome. If it is a palindrome, it checks if it's even or odd and increments the corresponding counter.

The function returns a tuple with the number of even and odd palindromes respectively.

The time complexity of this solution is O(n) because it needs to check each number in the range 1 to n. The space complexity is O(1) because it only uses a constant amount of space to store the counters and the current number.

You can test the function with the provided examples:

```
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)
```

This solution works for numbers up to 10^3 as required. For larger numbers, you might need to use a more efficient algorithm or a different approach.