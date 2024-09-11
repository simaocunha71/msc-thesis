"""
def get_coordinates(coordinate):
    x, y = coordinate
    result = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            result.append([x + i, y + j])
    return result

assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""

def get_coordinates(coordinate):
    x, y = coordinate
    result = [(x+i,y+j) for i in range(-1, 2) for j in range(-1, 2) if (i!=0 or j!=0)]
    return result

assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]

# 时间复杂度O(1)，空间复杂度O(1)
# 首先使用tuple解包，然后使用嵌套循环的方式生成所有的坐标，最后返回结果。

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

``