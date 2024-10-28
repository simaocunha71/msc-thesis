```
def max_Product(arr):
    arr.sort()
    if arr[-1] > 0:
        return arr[-1], arr[-2]
    else:
        return arr[0], arr[1]
```
This function first sorts the array in ascending order. Then, it checks if the last two elements are both positive. If they are, it returns the pair with the highest product (which is the product of the last two elements). If the last two elements are not both positive, it returns the pair with the highest product from the first two elements. 

The unit test `assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)` helps to clarify the problem by providing an example of the expected output. It shows that the function should return the pair with the highest product from the given array, even if the array contains zeros or negative numbers. 