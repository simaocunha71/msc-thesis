fibfib = {0: 0, 1: 0, 2: 1}

def fibfib(n: int) -> int:
    if n not in fibfib:
        fibfib[n] = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    return fibfib[n]




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

In this code, we first define a dictionary called `fibfib` to store the already computed FibFib numbers. We initialize it with the first three values of the FibFib sequence.

The `fibfib` function takes an integer `n` as input and checks if the `n`-th FibFib number is already computed and stored in the dictionary. If it is, the function simply returns the value from the dictionary. If it is not, the function computes the `n`-th FibFib number by recursively calling itself with `n-1`, `n-2`, and `n-3` as arguments, and stores the result in the dictionary. Finally, the function returns the computed `n`-th FibFib number.

This implementation is efficient because it avoids redundant computations by storing previously computed values in the dictionary.

```python
```

In this code, we define a function called `fibfib` that takes an integer `n` as input and returns the `n`-th FibFib number. We initialize a dictionary called `fibfib` with the first three values of the FibFib sequence.

The function first checks if the `n`-th FibFib number is already computed and stored in the dictionary. If it is, the function simply returns the value from the dictionary. If it is not, the function computes the `n`-th FibFib number by recursively calling itself with `n-1`, `n-2`, and `n-3` as arguments, and stores the result in