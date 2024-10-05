
    from collections import Counter

    def search(lst):
        freq = Counter(lst)
        max_num = max(lst)
        for i in range(max_num, 0, -1):
            if freq[i] >= i:
                return i
        return -1




# Here are some test cases to validate your code:
print(search([4, 1, 2, 2, 3, 1]))  # Expected: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Expected: 3
print(search([5, 5, 4, 4, 4]))  # Expected: -1
print(search([3, 2, 1]))  # Expected: -1
print(search([9, 9, 9, 9, 9]))  # Expected: -1
print(search([9, 9, 9, 9, 8]))  # Expected: 8
print(search([9, 9, 9, 9, 9, 9]))  # Expected: -1
print(search([1, 1, 1, 1, 1, 1]))  # Expected: -1
print(search([1, 1, 1, 1, 1, 2]))  # Expected: 1
print(search([1, 2, 3, 3, 3, 3, 4, 4, 4]))  # Expected: 3



































```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

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