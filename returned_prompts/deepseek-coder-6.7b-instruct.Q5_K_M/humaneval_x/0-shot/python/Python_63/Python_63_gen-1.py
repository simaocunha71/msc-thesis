
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c


def main():
    print(fibfib(1))  # 0
    print(fibfib(5))  # 4
    print(fibfib(8))  # 24


if __name__ == "__main__":
    main()

```

## Solution
```python
def fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c

def main():
    print(fibfib(1))  # 0
    print(fibfib(5))  # 4
    print(fibfib(8))  # 24

if __name__ == "__main__":
    main()
```

## Explanation
The function `fibfib(n)` calculates the n-th element of the FibFib number sequence. The base cases are defined as `fibfib(0) == 0` and `fibfib(1) == 0`, and `fibfib(2) == 1`. 

For `n > 2`, the function uses a loop to calculate the n-th element. It keeps track of the last three elements of the sequence in variables `a`, `b`, and `c`. In each iteration of the loop, it updates `a`, `b`, and `c` to the next values in the sequence, which are `b`, `c`, and `a+b+c` respectively. 

Finally, it returns `c`, which is the n-