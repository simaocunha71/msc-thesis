def count_Pairs(list_int, n):
    count = 0
    for i in range(len(list_int)):
        for j in range(i + 1, len(list_int)):
            if list_int[i] != list_int[j]:
                count += 1
    return count

# Test
print(count_Pairs([1, 2, 1], 3))  # Output: 2
"""
The time complexity of this function is O(n^2) because it uses two nested loops to iterate through all possible pairs of elements in the list.
"""

# Space complexity is O(1) as it uses a fixed amount of space to store the count variable, regardless of the size of the input list.

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```