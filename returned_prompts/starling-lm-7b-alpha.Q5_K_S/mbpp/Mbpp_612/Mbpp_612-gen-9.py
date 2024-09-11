def merge(l):
    first_list = []
    second_list = []
    for sublist in l:
        first_list.append(sublist[0])
        second_list.append(sublist[1])
    return [first_list, second_list]

merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) # returns [['x', 'a', 'm'], ['y', 'b', 'n']]

# Time complexity: O(n), where n is the number of sublists in the input list.
# Space complexity: O(n), where n is the number of sublists in the input list.

# Alternatively, we could have used list comprehensions to achieve the same result:

def merge(l):
    return [l[i][0] for i in range(len(l))], [l[i][1] for i in range(len(l))]

# Time complexity: O(n), where n is the number of sublists in the input list.
# Space complexity: O(n), where n is the number of sublists in the input list.

# However, using list comprehensions may be less readable and harder to understand for those unfamiliar with the syntax.

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
