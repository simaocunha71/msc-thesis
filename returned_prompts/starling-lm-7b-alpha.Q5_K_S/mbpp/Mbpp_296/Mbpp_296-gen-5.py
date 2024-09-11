"""
def get_Inv_Count(a):
    result = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                result += 1
    return result
"""

def get_Inv_Count(a):
    result = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                result += 1
    return result



"""
def get_Inv_Count(a):
    result = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                result += 1
    return result
"""


"""
def get_Inv_Count(a):
    result = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                result += 1
    return result
"""

def test_get_Inv_Count():
    assert get_Inv_Count([1,20,6,4,5]) == 5

test_get_Inv_Count()
print('All tests passed.')

# Made By Mostafa_Khaled
```
 Here is a Python function to count inversions in an array:

```python
def get_Inv_Count(a):
    result = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                result += 1
    return result
```

This function takes an array `a` as input and initializes a variable `result` to zero. It then iterates through the array using two nested loops. For each pair of elements `(a[i], a[j])` in the array, if `a[i]` is greater than `a[j]`, it increments the `result` variable by one