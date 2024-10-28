The task is to create a function that counts the pairs of strings in a given list where the strings are reverse of each other.

Here's the Python function that solves the problem:

```Python
def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j][::-1] or lst[j] == lst[i][::-1]:
                count += 1
    return count
```

This function works by iterating over each string in the list and comparing it with every other string in the list. If a string is the reverse of another string, it increments the count. The function then returns the count.

The unit test `assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2` passes because the function correctly identifies that "julia" and "ailuj" are reverse pairs, and "tseb" and "best" are also reverse pairs. Therefore, the total count of reverse pairs is 2. 





Python code:

```Python
def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j][::-1] or lst[j] == lst[i][::-1]:
                count += 1
    return count

assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
```

Output:

```Python
2
```





Explanation:

The function `count_reverse_pairs(lst)` iterates over the list of strings and checks if the current string is the reverse of any other string in the list. If it finds a match, it increments the count. The function returns the count of reverse pairs.

The unit test `assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2` checks if the function correctly identifies the reverse pairs in the given list. The expected output is 2, which is the correct count of reverse pairs.