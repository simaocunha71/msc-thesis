"""
def test_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
"""

def test_duplicate(arr):
    return len(arr) != len(set(arr))

#assert test_duplicate([1,2,3,4,5])==False
#assert test_duplicate([1,1,2,3,4,5])==True
print(test_duplicate([1,1,2,3,4,5]))

# This solution is a bit faster
# https://stackoverflow.com/questions/1732013/fastest-way-to-check-if-a-list-contains-duplicates-in-python/9028109#9028109
```

In this problem, we can easily solve the problem by using Python built-in function set(), which only keeps the unique values of the input array. If the length of the array is not equal to the length of the set, it means there are duplicate elements in the array.

The time complexity of this solution is O(n), and the space complexity is O(n).

```
def test_duplicate(arr):
    return len(arr) != len(set(arr))
```
```

In this problem, we can easily solve the problem by using Python built-in function set(), which only keeps the unique values of the input array. If the length of the array is not equal to the length of the set, it means there are duplicate elements in the array.

The time complexity of this solution is O(n), and the space complexity is O(n).

```
def test_duplicate(arr):
    return len(arr) != len(set(arr))
```

```python
def test_duplicate(arr):
    return len(arr) != len(set(arr))
```

In this problem, we can easily solve the problem by using Python built-in function set(), which only keeps the unique values of the input array. If the length of the array is not