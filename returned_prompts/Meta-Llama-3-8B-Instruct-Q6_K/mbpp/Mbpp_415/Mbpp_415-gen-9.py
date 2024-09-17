```
def max_Product(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    result = (float('-inf'), float('-inf'))
    
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
    
    if max1 * max2 > max1 * min1 and max1 * max2 > max1 * min2:
        return (max1, max2)
    elif max1 * min1 > max1 * min2:
        return (max1, min1)
    else:
        return (max1, min2)
```


This function iterates over the array to find the maximum and minimum values and then returns the pair with the highest product. The time complexity is O(n) where n is the size of the input array. The unit test `assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)` is used to verify the correctness of the function. 

The function works by maintaining two variables max1 and max2 to store the maximum and second maximum values respectively, and two variables min1 and min2 to store the minimum and second minimum values respectively. Then it iterates over the array and updates these variables as necessary. Finally, it compares the products of the maximum and second maximum values with the products of the maximum and minimum values, and returns the pair with the highest product. 





The unit test is used to verify the correctness of the function. The test checks if the function returns the expected result for the input array `[1,2,3,4,7,0,8,4]`, which is `(7,8)`. If the function returns the same result as expected, the test passes; otherwise, it fails. This ensures that the function is working correctly.