"""
def tetrahedral_number(n):
    return n * (n + 1) * (n + 2) // 6

# The above can be simplified to:
def tetrahedral_number(n):
    return (n + 1) * (n + 2) * n // 6

# The above can be further simplified to:
def tetrahedral_number(n):
    return (n + 1) * (n + 2) * (n >> 1)
"""

def tetrahedral_number(n):
    return (n + 1) * (n + 2) * (n >> 1)

# print(tetrahedral_number(5))

# 以下是其他答案
def tetrahedral_number(n):
    return (n + 1) * (n + 2) * (n + 3) // 6 - 1

def tetrahedral_number(n):
    return (n + 1) * (n + 2) * (n + 3) // 6


```
解释：
这个问题是要找到第n个四面体数。四面体数是从1开始的一个数列，第n个数等于n * (n + 1) * (n + 2) / 6。

```python
def tetrahedral_number(n):
    return (n + 1) * (n + 2) * (n >> 1)
```

这个函数的实现是将n + 1、n + 2、n右移一位（相当于除以2），然后将这三个数相乘得到第n个四面体数。右移一位相当于将一个数除以2，所以这个实现是正确的。
```python
def tetrahedral_number(n):
    return (n + 1) * (n + 2) * (n >> 1)
```

这个函数的实现是将n + 1、n + 2、n右