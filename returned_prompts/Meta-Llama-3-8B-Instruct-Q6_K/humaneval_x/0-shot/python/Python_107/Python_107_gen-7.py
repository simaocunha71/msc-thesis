```
def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            even_count += 1
        elif str(i) == str(i)[::-1] and i % 2 != 0:
            odd_count += 1
    return (even_count, odd_count)
```



Explanation:
The problem requires us to find the number of even and odd integer palindromes within the range(1, n). We can solve this by iterating over the range and checking if each number is a palindrome and if it's even or odd.

We initialize two counters, `even_count` and `odd_count`, to keep track of the number of even and odd palindromes respectively.

For each number `i` in the range, we convert it to a string and check if it's equal to its reverse. If it is, then it's a palindrome. We then check if `i` is even or odd using the modulo operator `%`.

If `i` is even and a palindrome, we increment `even_count`. If `i` is odd and a palindrome, we increment `odd_count`.

Finally, we return a tuple containing the counts of even and odd palindromes.

The time complexity of this solution is O(n), where n is the input number, because we're iterating over the range once. The space complexity is O(1), because we're using a constant amount of space to store the counters.