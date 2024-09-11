"""
The definition of Perrin number is as follows:
1 is a Perrin number,
If n is a Perrin number, then n + 1 is a Perrin number,
If n is a Perrin number, then 2n + 1 is a Perrin number.

Here is a Python solution to this problem:
"""


def cal_sum(n):
    """
    Args:
        n: The max number of Perrin number to be calculated.

    Returns:
        The sum of all Perrin number from 1 to n.
    """
    result = 0
    p_list = [1]
    for i in range(n):
        p_list.append(2 * p_list[i] + 1)
        p_list.append(p_list[i] + 1)
        result += sum(p_list[-2::-1])
    return result


print(cal_sum(9))
"""
This is the solution to this problem, and you can verify it by running the code.
"""


"""
In this code, we first initialize the result to 0, and the Perrin number list is initialized with 1.
Then we start a for loop, with each iteration, we add two Perrin numbers to the list, one is 2 times the previous Perrin number, and the other is the previous Perrin number plus 1.
After adding these two numbers, we add all the numbers in the Perrin number list from the second to the last to the result.
Finally, we return the result.
"""

# 
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