
def even_odd_palindrome(n):
    even_palindrome_count = 0
    odd_palindrome_count = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_palindrome_count += 1
            else:
                odd_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)


# Time:  O(n)
# Space: O(1)

```
```
"""
def even_odd_palindrome(n):
    even_palindrome_count = 0
    odd_palindrome_count = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_palindrome_count += 1
            else:
                odd_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)


# Time:  O(n)
# Space: O(n)
class Solution(object):
    def evenOddPalindrome(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def is_palindrome(x):
            return str(x) == str(x)[::-1]
        even_palindrome_count = sum(i for i in xrange(1, n+1) if is_palindrome(i) and i % 2 == 0)
        odd_palindrome_count = sum(i for i in xrange(1, n+1) if is_palindrome(i) and i % 2 != 0)
        return [even_palindrome_count, odd_palindrome_count]
"""
```
```
```


```
```
```
```
```
```
```
```