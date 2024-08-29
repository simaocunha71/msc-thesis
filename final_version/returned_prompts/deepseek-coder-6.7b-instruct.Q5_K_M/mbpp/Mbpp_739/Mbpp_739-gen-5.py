"""
We know that triangular numbers are given by the formula n*(n+1)/2.
We need to find the smallest index 'n' such that n*(n+1)/2 has 'n' digits.
We can start from n=1 and keep incrementing n until we find the smallest 'n' such that the number n*(n+1)/2 has 'n' digits.
"""

def find_Index(n):
    i = 1
    while True:
        num = i*(i+1)//2
        if len(str(num)) == n:
            return i
        i += 1

print(find_Index(2))  # Output: 4
"""
Explanation:
The smallest triangular number with 2 digits is 10 and its index is 4.
"""
```

**Example 2:**

```python
