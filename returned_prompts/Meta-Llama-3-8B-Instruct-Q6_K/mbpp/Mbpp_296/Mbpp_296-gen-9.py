```
def get_Inv_Count(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count
```


The function `get_Inv_Count` counts the number of inversions in the given array. An inversion is a pair of elements in the array that are in the wrong order. For example, in the array [1,20,6,4,5], the pairs (20,1), (6,1), (6,4), (20,4) and (5,4) are inversions. The function iterates over the array and checks for every pair of elements if they are in the wrong order, if they are, it increments the inversion count. The function then returns the total inversion count. The unit test `assert get_Inv_Count([1,20,6,4,5]) == 5` ensures that the function correctly counts the inversions in the array. 







