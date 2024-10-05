fib4_list = [0, 0, 2]
while len(fib4_list) < 80:
    fib4_list.append(fib4_list[-1] + fib4_list[-2] + fib4_list[-3] + fib4_list[-4])

def fib4(n: int):
    if n < len(fib4_list):
        return fib4_list[n]
    else:
        raise IndexError("fib4 index out of range")

fib4(5) # 4
fib4(6) # 8
fib4(7) # 14



# Created by Leonyard on 2020/06/06
# Last Modified by Leonyard on 2020/06/06
# Licensed under MIT License.
# Copyright (c) 2020 Leonyard
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
