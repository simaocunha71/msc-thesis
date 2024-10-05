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


Explanation:

The function `get_max_triples(n)` generates an array `a` of length `n` using a list comprehension, where each element is calculated as `i * i - i + 1` for `i` in the range from 1 to `n`.

Then, the function iterates over all possible triples `(a[i], a[j], a[k])` of the array `a`, where `i < j < k`. For each triple, it checks if their sum is a multiple of 3 by using the modulo operator (`%`). If the sum is a multiple of 3, it increments the count of valid triples.

Finally, the function returns the count of valid triples.

For the given example `n = 5`, the function generates the array `a = [1, 3, 7, 13, 21]` and finds that the only valid triple is `(1, 7, 13)`, so the function returns `1`.