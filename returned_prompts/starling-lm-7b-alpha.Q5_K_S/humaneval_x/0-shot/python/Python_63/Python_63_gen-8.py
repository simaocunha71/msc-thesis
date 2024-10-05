fib_fib_cache = {}


def fibfib(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    elif n in fib_fib_cache:
        return fib_fib_cache[n]
    else:
        fib_fib_cache[n] = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
        return fib_fib_cache[n]

# To pass the doctests
fibfib = staticmethod(fibfib)




# Made By Mostafa_Khaled
```

1
2
3
4
5
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