```
def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        n -= 2
        a, b = 1, 1
        for _ in range(n):
            a, b = b, (2*a+b)%2
        return b
```

Here's a function to generate a jacobsthal number given the index of the number in the sequence.
The Jacobsthal numbers can be generated using the recurrence relation:
$J_n = 2J_{n-1} + J_{n-2}$ with $J_0 = 0$, $J_1 = 1$, and $J_2 = 1$.

For example, to generate the 5th number in the sequence, we can follow these steps:

- Initialize $a=1$ and $b=1$ (the first two numbers in the sequence).
- Iterate $n-2$ times (since we've already generated the first two numbers), in each iteration, update $a$ to be equal to $b$ and $b$ to be equal to $2a+b$ (mod 2).
- The resulting value of $b$ is the $n$th Jacobsthal number.

In python, this can be implemented as follows:

```python
def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        n -= 2
        a, b = 1, 1
        for _ in range(n):
            a, b = b, (2*a+b)%2
        return b
```

We can verify this function is correct by checking that it returns the correct values for the first few numbers in the sequence:

```python
print(jacobsthal_num(0) == 0)  # True
print(jacobsthal_num(1) == 1)  # True
print