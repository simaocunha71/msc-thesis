def count_Pairs(arr,n):
    arr.sort()
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i] != arr[j]):
                count += 1
    return count

# Driver code
arr = [1,2,1]
n = len(arr)
print(count_Pairs(arr,n))
"""
The time complexity of this algorithm is O(n^2)
The space complexity of this algorithm is O(n)
"""

# This code is contributed by PrinciRaj15
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
```
```
```
```
```
```
```
```
```
``