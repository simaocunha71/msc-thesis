    from math import log
    from math import log2
    from math import log10
    from math import log1p
    from math import logb
    from math import loggcd
    from math import log2p
    from math import logb
    from math import loggcd

    # Your code goes here
    def is_simple_power(x, n):
        if n < 2:
            return x == n
        else:
            return x == int(log(x, n)) ** int(log(n, n))

    return is_simple_power(x, n)






```
def is_simple_power(x, n):
    """
    Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """

    from math import log
    from math import log2
    from math import log10
    from math import log1p
    from math import logb
    from math import loggcd
    from math import log2p
    from math import logb
    from math import loggcd

    # Your code goes here
    def is_simple_power(x, n):
        if n < 2:
            return x == n
        else:
            return x == int(log(x, n)) ** int(log(n, n))

    return is_simple_power(x, n)
```
```python
def is_simple_power(x, n):
    """
    Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n