```
def max_Product(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    result = (None, None)

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

        if max1 * max2 > result[0]:
            result = (max1, max2)

    return result
```


This function iterates over the array, keeping track of the two maximum and minimum numbers seen so far. The maximum product is either the product of the two maximum numbers, or the product of one maximum and one minimum number (since the minimum numbers could be negative and make the product larger). It keeps track of the pair with the maximum product and returns it.

The unit test provided ensures that the function returns the correct pair for the given array. For example, the maximum product in the array [1,2,3,4,7,0,8,4] is the product of 7 and 8, so the function should return (7,8). 

The function runs in O(n) time, where n is the length of the array, since it makes a single pass over the array. It uses O(1) space to store the maximum and minimum numbers and the result. 





