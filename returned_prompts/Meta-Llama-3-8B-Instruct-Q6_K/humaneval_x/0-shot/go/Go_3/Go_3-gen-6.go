
This problem can also be solved using a one-liner in Python:

```Python
def BelowZero(operations):
    return any(balance < 0 for balance in (acc := [0]) + [acc[-1