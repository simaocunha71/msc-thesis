
Here is a Python solution that implements the problem description:

```
def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count
```

This function creates an array `a` of length `n` where each element is calculated as `i * i - i + 1`. Then, it uses three nested loops to iterate over all possible triples `(a[i], a[j], a[k])` where `i < j < k`. If the sum of the triple is a multiple of 3, it increments the count. Finally, it returns the count of valid triples.

For example, if `n = 5`, the function will return `1` because there is only one valid triple `(1, 7, 13)`.

Note that the time complexity of this solution is O(n^3) because it uses three nested loops. If `n` is large, this solution may be slow. A more efficient solution might be possible using a different algorithm or data structure.