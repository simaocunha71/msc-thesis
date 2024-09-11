Here is a solution for the above problem:

```python
def sum_in_range(l,r):
    if l%2 == 0 and r%2 == 0:
        return l + r
    elif l%2 != 0 and r%2 != 0:
        return (l + r) + sum_in_range(l+1,r-1)
    else:
        if l%2 != 0:
            return (l + r) + (l + 1)//2
        else:
            return (l + r) + r//2
```

Explanation:
This function will find the sum of all odd natural numbers within the range from l to r. It does so by recursively adding the odd numbers in the range.

If both l and r are even, it simply returns the sum of l and r.

If both l and r are odd, it adds l, r, and the sum of all odd numbers from l+1 to r-1 (i.e., the sum of all odd numbers in the range from l+1 to r-1).

If l is odd and r is even, it adds l, r, and the sum of all odd numbers from l+1 to r (i.e., the sum of all odd numbers from l+1 to r).

If l is even and r is odd, it adds l, r, and the sum of all odd numbers from l to r-1 (i.e., the sum of all odd numbers from l to r-1).

For example, if we call `sum_in_range(2,5)`, it will return 8, because the odd numbers in the range from 2 to 5 are 3, 5, and 7, and their sum is 8.
```

In this case, the function `sum_in_range(2,5)` is called with the arguments 2 and 5. The function first checks if both 2 and 5 are even numbers. Since 2 is even and 5 is odd, the function returns the sum of all odd numbers in the range from 2 to 5. It does this by recursively adding the odd numbers from 2+1 to 5-1, which are 3, 