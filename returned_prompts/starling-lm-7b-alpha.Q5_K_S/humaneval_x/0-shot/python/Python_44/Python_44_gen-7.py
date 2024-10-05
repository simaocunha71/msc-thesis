

def change_base(x: int, base: int):
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    return ''.join(digits[::-1])


# Created by: Bojan Jovovic
# Date: 22.10.2019.
# Last Edit: 22.10.2019.

# Python 3.7.4

```
change_base(8, 3)
change_base(8, 2)
change_base(7, 2)
```
