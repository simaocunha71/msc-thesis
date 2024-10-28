
def sum_squares(lst):
    # Initialize result
    result = 0
    # Iterate through the list
    for i in range(len(lst)):
        # Square the number if index is a multiple of 3
        if (i+1) % 3 == 0:
            lst[i] = lst[i] ** 2
        # Cube the number if index is a multiple of 4 and not a multiple of 3
        elif (i+1) % 4 == 0 and (i+1) % 3 != 0:
            lst[i] = lst[i] ** 3
        # Add the number to the result
        result += lst[i]
    return result


# Test Cases
print(sum_squares([1,2,3])) # Output: 6
print(sum_squares([])) # Output: 0
print(sum_squares([-1,-5,2,-1,-5])) # Output: -126


































































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

