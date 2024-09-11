from typing import List


def diff_even_odd(nums: List[int]) -> int:
    evens = [num for num in nums if num % 2 == 0]
    odds = [num for num in nums if num % 2 == 1]
    return evens[0] - odds[0] if evens and odds else 0


print(diff_even_odd([1,3,5,7,4,1,6,8]))







"""

"""

# Time Complexity: O(n)
# Space Complexity: O(n)


# Test Cases
print(diff_even_odd([1,3,5,7,4,1,6,8]))  # 3
print(diff_even_odd([1,3,5,7,8,1,6,4]))  # 4
print(diff_even_odd([8,1,4,9,1,3]))  # -5
print(diff_even_odd([-2, 0, -1, 2]))  # 0
print(diff_even_odd([1,3,5]))  # 0
print(diff_even_odd([]))  # 0
print(diff_even_odd([-1]))  # 0
print(diff_even_odd([1,2,3,4,5,6,7,8]))  # 2
print(diff_even_odd([-1,0,1,2,3,4,5,6,7,8]))  # 2




"""

"""



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