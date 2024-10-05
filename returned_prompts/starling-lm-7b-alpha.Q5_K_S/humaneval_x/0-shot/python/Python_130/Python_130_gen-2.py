
def tri(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 3]
    if n % 2 == 0:
        return [1, 3, 2] + tri(n - 2)
    else:
        return [1, 3, 2] + tri(n - 3) + tri(n - 2)


#print(tri(3))




```



```

```