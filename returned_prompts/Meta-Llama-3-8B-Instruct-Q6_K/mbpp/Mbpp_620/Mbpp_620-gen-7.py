```
def largest_subset(numbers):
    numbers = sorted(set(numbers))
    max_subset = 0
    for i in range(len(numbers)):
        subset_size = 1
        for j in range(i + 1, len(numbers)):
            if numbers[j] % numbers[i] == 0:
                subset_size += 1
            else:
                break
        max_subset = max(max_subset, subset_size)
    return max_subset
```







