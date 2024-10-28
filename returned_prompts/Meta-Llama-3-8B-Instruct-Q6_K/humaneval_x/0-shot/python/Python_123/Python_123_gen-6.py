```
def get_odd_collatz(n):
    result = []
    while n != 1:
        if n % 2 != 0:  # if n is odd
            result.append(n)
        if n % 2 == 0:  # if n is even
            n = n // 2
        else:
            n = n * 3 + 1
    return sorted(result)
```



Explanation:
1. Initialize an empty list `result` to store the odd numbers in the Collatz sequence.
2. Start a loop that continues until `n` becomes 1.
3. Inside the loop, check if `n` is odd or even. If `n` is odd, append it to the `result` list.
4. If `n` is even, divide it by 2. If `n` is odd, multiply it by 3 and add 1.
5. After the loop, return the `result` list sorted in increasing order using the `sorted()` function.

For example, if the input is 5, the function will return `[1, 5]`, which are the odd numbers in the Collatz sequence for 5.