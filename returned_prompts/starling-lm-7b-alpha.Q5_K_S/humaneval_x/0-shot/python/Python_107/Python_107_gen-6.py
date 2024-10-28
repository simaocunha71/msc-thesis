
# Time:  O(n)
# Space: O(1)

def even_odd_palindrome(n):
    # Initialize result.
    result = (0, 0)

    # Initialize left and right.
    left, right = 1, 1

    # While left is less than or equal to n.
    while left <= n:
        # If left is even, increment result.even.
        if left % 2 == 0:
            result = (result[0] + 1, result[1])
        # If left is odd, increment result.odd.
        else:
            result = (result[0], result[1] + 1)

        # Increment left and right by one.
        left += 1
        right += 1

        # While left is less than right and right is palindrome, decrement right.
        while str(left) != str(right)[::-1]:
            right -= 1

    return result

# Time:  O(n)
# Space: O(n)
class Solution(object):
    def even_odd_palindrome(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        even, odd = 0, 0
        for i in xrange(1, n+1):
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
            while str(i) != str(i)[::-1]:
                if i % 2 == 0:
                    even -= 1
                else:
                    odd -= 1
                i -= 1
        return [even, odd]


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

```

```

```
