def pair_wise(lst):
    result = []
    for i in range(len(lst)-1):
        result.append((lst[i], lst[i+1]))
    return result


# Alternative:
def pair_wise(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]

# Alternative:
def pair_wise(lst):
    return [(x, y) for x, y in zip(lst[:-1], lst[1:])]


# Alternative:
def pair_wise(lst):
    return list(zip(lst[:-1], lst[1:]))

# Alternative:
def pair_wise(lst):
    return list(zip(lst, lst[1:]))



# Complexity Analysis
# Time Complexity: O(n)
# Space Complexity: O(1)



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

```

```

```

```

```

