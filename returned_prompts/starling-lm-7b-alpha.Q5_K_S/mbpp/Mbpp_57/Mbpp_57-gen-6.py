from itertools import permutations
def find_Max_Num(lis):
    perm = permutations(lis)
    max = 0
    for i in perm:
        i = int("".join(map(str,i)))
        if i > max:
            max = i
    return max

# Driver Code
lis = [1, 2, 3]
print(find_Max_Num(lis))
"""
Output:
321
"""

# Time complexity: O(n!)
# Space complexity: O(n)

# This code is Contributed By Amit Khandelwal


# This code is contributed by Rian Xu
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
