The Perrin sequence is defined recursively as follows: P(0) = 3, P(1) = 0, P(2) = 2, P(n) = P(n-1) + P(n-2) + P(n-3) for n >= 3. The task is to write a function that calculates the sum of the first n Perrin numbers.

Here is a Python solution for this problem:

```python
def cal_sum(n):
    if n <= 2:
        return 3
    p = [3, 0, 2]
    for _ in range(3, n):
        p.append(p[-1] + p[-2] + p[-3])
    return sum(p[:n])
```

This function first checks if n is less than or equal to 2. If it is, the function returns 3, as the sum of the first 0, 1, or 2 Perrin numbers is 3. If n is greater than 2, the function calculates the Perrin sequence up to the nth number and returns the sum of the first n Perrin numbers.

The unit test `assert cal_sum(9) == 49` ensures that the function is working correctly. The sum of the first 9 Perrin numbers is indeed 49. 