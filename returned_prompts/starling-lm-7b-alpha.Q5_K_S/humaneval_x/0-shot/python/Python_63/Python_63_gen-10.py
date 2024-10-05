fibfib_cache = [0, 0, 1]

def fibfib(n: int):
    if n < len(fibfib_cache):
        return fibfib_cache[n]
    else:
        fibfib_cache.append(fibfib(n-1) + fibfib(n-2) + fibfib(n-3))
        return fibfib_cache[n]

fibfib_cache = [0, 0, 1]

def fibfib(n: int):
    if n < len(fibfib_cache):
        return fibfib_cache[n]
    else:
        fibfib_cache.append(fibfib(n-1) + fibfib(n-2) + fibfib(n-3))
        return fibfib_cache[n]



```

```
from typing import List

def fibfib(n: int) -> int:
    fibfib_cache = [0, 0, 1]
    while len(fibfib_cache) <= n:
        fibfib_cache.append(fibfib_cache[-1] + fibfib_cache[-2] + fibfib_cache[-3])
    return fibfib_cache[n]
```

However, it's worth noting that the FibFib sequence is just the Fibonacci sequence shifted by one. The Fibonacci sequence can be computed in $O(\log n)$ time using matrix exponentiation or $O(\sqrt{n})$ time using a closed-form expression.

```python
import math
from typing import List

def fibonacci(n: int) -> int:
    if n < 2:
        return n
    else:
        # Using the closed-form expression for the nth Fibonacci number
        golden_ratio = (1 + math.sqrt(5)) / 2
        fib_n = math.floor((golden_ratio**n + (1 - golden_ratio)**n) / math.sqrt(5))
        return fib_n

def fibfib(