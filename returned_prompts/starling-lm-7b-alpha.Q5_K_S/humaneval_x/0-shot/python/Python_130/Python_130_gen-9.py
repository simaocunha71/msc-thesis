
def tri(n):
    if n==0:
        return []
    if n==1:
        return [1]
    if n==2:
        return [1,3]
    if n==3:
        return [1,3,2]
    if n%2==0:
        return [1,3,2]+tri(n-2)
    else:
        return [1,3,2]+tri(n-2)+[tri(n+1)]



```

```
def tri(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,3]
    elif n == 3:
        return [1,3,2]
    elif n % 2 == 0:
        return [1,3,2] + tri(n-2)
    else:
        return [1,3,2] + tri(n-2) + [tri(n+1)]
```

This solution is based on the recurrence relation of the Tribonacci sequence.
The function `tri` takes a non-negative integer `n` as an argument and returns a list of the first n + 1 numbers of the Tribonacci sequence. 

The function first checks if `n` is 0, 1, 2, or 3 and returns the corresponding result directly. 

If `n` is even, the function appends the first three numbers of the Tribonacci sequence (1, 3, 2) to the result of `tri(n-2)` and returns it. 

If `n` is odd, the function appends the first three numbers of the Tribonacci sequence (1, 3, 2) to the result of `tri(n-2)` and the result of `tri(n+1)`, and returns it. 

This recursive approach allows the function to generate the Tribonacci sequence efficiently. 

The time complexity of this solution is O(n), where n is the input value. 

The space complexity is also O(n) due to the recursive calls stack and the result list.
``