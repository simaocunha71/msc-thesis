"""
def sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 4
    elif n == 3:
        return 10
    else:
        return sequence(n - 1) + sequence(n - 2) + sequence(n - 3)
    """


def sequence(n):
    if n < 4:
        return n
    else:
        return sequence(n - 1) + sequence(n - 2) + sequence(n - 3)


assert sequence(10) == 6
print(sequence(10))

```
1. 请简单介绍一下新曼-康威序列？
2. 请简单介绍一下递归和迭代两种解决问题的思路？
3. 请简单介绍一下递归和迭代的时间复杂度和空间复杂度？

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
