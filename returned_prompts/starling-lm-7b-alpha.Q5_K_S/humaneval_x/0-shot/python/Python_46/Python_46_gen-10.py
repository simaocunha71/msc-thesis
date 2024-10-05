fib4 = [0]*5 + [None]*1000
fib4[0] = 0
fib4[1] = 0
fib4[2] = 2
fib4[3] = 0
for i in range(4, 1000):
    fib4[i] = fib4[i-1] + fib4[i-2] + fib4[i-3] + fib4[i-4]
    #print(fib4[i])




def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

    if n < 5:
        return fib4[n]
    fib4[5:n+1] = [fib4[i-1] + fib4[i-2] + fib4[i-3] + fib4[i-4] for i in range(5, n+1)]
    return fib4[n]


# Made By Mostafa_Khaled
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
```
```

```
```
```
```
```
