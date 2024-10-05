```
def get_max_triples(n):
    a = [i**2 - i + 1 for i in range(1, n+1)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count
```


This function first generates the array `a` according to the given formula. Then, it iterates over the array and checks for each triple `(a[i], a[j], a[k])` whether their sum is a multiple of 3. If it is, it increments the count. Finally, it returns the count. 

The time complexity of this function is O(n^3) because it has three nested loops that each run up to `n` times. The space complexity is O(n) because it needs to store the array `a` with `n` elements. 

Note that this function is not very efficient for large values of `n` because of its high time complexity. If `n` is very large, you may need to use a more efficient algorithm or a more efficient language. 







