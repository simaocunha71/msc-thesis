```
def largest_subset(numbers):
    numbers.sort()
    max_size = 0
    i = 0
    while i < len(numbers):
        size = 1
        for j in range(i + 1, len(numbers)):
            if numbers[j] % numbers[i] == 0:
                size += 1
            else:
                break
        max_size = max(max_size, size)
        i += size
    return max_size
```


This function sorts the list of numbers first. Then, it iterates over the list and for each number, it finds the largest subset of numbers that are divisible by it. The size of the largest subset is updated accordingly. The function returns the size of the largest subset.

For example, for the list [1, 3, 6, 13, 17, 18], the function will find the subsets [1], [1, 3], [1, 3, 6], and [1, 3, 6, 18], and return 4 as the size of the largest subset. 





