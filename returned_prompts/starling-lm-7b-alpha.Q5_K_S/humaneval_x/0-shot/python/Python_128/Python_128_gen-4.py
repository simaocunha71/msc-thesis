    # Your solution here
    if len(arr) == 0:
        return None
    sign = 1
    sum = 0
    for i in arr:
        if i == 0:
            continue
        elif i > 0:
            sign *= 1
        elif i < 0:
            sign *= -1
        sum += abs(i)
    return sign * sum





# Made By Mostafa_Khaled
```

```
#!/usr/bin/env python
from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip


def main():
    print(prod_signs([1, 2, 2, -4]))
    print(prod_signs([0, 1]))
    print(prod_signs([]))


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).