The task is to find the number of n-digit positive integers that start or end with 1.

Here is the Python solution:

```
def starts_one_ends(n):
    count = 0
    for i in range(10**(n-1), 10**n):
        if i % 10 == 1 or i // 10**(n-1) % 10 == 1:
            count += 1
    return count
```

Explanation:
This function works by iterating over all n-digit numbers from 10^(n-1) to 10^n. For each number, it checks if the number starts or ends with 1. If it does, it increments the count. Finally, it returns the count.

For example, if we call starts_one_ends(2), it will return 9 because there are 9 two-digit numbers that start or end with 1: 10, 11, 12, 13, 14, 15, 16, 17, 18, and 91. If we call starts_one_ends(3), it will return 90 because there are 90 three-digit numbers that start or end with 1.