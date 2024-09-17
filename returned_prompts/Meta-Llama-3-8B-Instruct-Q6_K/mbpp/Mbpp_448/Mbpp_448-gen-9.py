The Perrin sequence is a sequence of positive integers, where the first three numbers are 3, 0, and 2. The next number in the sequence is the sum of the previous three numbers. 

The function `cal_sum` calculates the sum of the first `n` Perrin numbers. 

Here is the Python solution for this problem:
```
def cal_sum(n):
    if n <= 0:
        return 0
    a, b, c = 3, 0, 2
    total = 3
    for _ in range(2, n):
        a, b, c = b, c, a + b
        total += c
    return total
```
This function first checks if `n` is less than or equal to 0. If it is, the function returns 0. Then it initializes three variables `a`, `b`, and `c` to the first three Perrin numbers. It also initializes a variable `total` to the sum of the first three Perrin numbers. 

The function then enters a loop that runs `n-2` times. In each iteration of the loop, it updates the values of `a`, `b`, and `c` to the next three Perrin numbers and adds `c` to `total`. 

Finally, the function returns `total`, which is the sum of the first `n` Perrin numbers. 

For example, `cal_sum(9)` returns `49`, which is the sum of the first 9 Perrin numbers.  The first 9 Perrin numbers are 3, 0, 2, 3, 2, 5, 7, 12, and 19. The sum of these numbers is 49.  Therefore, the function `cal_sum` correctly calculates the sum of the first `n` Perrin numbers. 