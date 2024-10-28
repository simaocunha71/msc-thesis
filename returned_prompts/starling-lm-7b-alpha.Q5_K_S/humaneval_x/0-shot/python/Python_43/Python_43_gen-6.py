    l.sort()
    n = len(l)
    for i in range(n):
        if i + 1 < n and l[i] + l[i + 1] == 0:
            return True
        if i + 2 < n and l[i] + l[i + 2] == 0:
            return True
    return False



# Define the function pairs_sum_to_zero here:



# Add your test cases here:



# Add your assertions here:



```
1
```
