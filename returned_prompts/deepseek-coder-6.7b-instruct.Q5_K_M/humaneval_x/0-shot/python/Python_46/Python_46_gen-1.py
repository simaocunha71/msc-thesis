
```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib = [0, 0, 2, 0]

    for i in range(4, n + 1):
        fib.append(fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4])

    return fib[n]
```

Explanation:
This function uses dynamic programming to keep track of the previous 4 numbers in the sequence. It starts by initializing the first 4 numbers of the sequence. Then it iteratively calculates the next number in the sequence by adding the previous 4 numbers. This is done until the n-th number is calculated. The n-th number is then returned.

This function has a time complexity of O(n) because it needs to iterate over the range of numbers from 4 to n. The space complexity is also O(n) because it stores the entire sequence up to the n-th number.

Test this function with the given test cases to verify it's working correctly.
"""

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This function should return the correct results for the test cases.
"""

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This function should return the correct results for the test cases.
"""

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(fib4(7))  # 14
```

This function should return the correct results for the test cases.
"""

# Test cases
print(fib4(5))  # 4
print(fib4(6))  # 8
print(f