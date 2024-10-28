```
def max_Product(arr):
    if len(arr) < 2:
        return None
    arr.sort()
    return (arr[-1], arr[-2])
```
This function takes an array of integers as an argument. It first checks if the array has less than two elements. If so, it returns None. Otherwise, it sorts the array in ascending order and returns the last two elements of the sorted array, which are the maximum product pair. The unit test `assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)` shows that the function should return the pair with the highest product, not the pair with the highest sum. The product of 7 and 8 is indeed the highest among all possible pairs in the given array. 





