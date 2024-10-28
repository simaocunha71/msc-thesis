```
def max_Product(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    res1 = res2 = 0

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

    return max1*max2, max1*min1
```
This function initializes two variables max1 and max2 to keep track of the two maximum numbers in the array, and two variables min1 and min2 to keep track of the two minimum numbers. It then iterates over the array, updating these variables as necessary. Finally, it returns the product of the two maximum numbers, and the product of the two maximum numbers and the smallest number. 

This solution assumes that the array contains at least two distinct numbers. If the array could contain fewer than two distinct numbers, the problem statement would need to be modified to specify what should happen in that case. 

The unit test `assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)` confirms that the function should return the pair with the highest product, which in this case is (7,8). 
```
def max_Product(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    res1 = res2 = 0

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

    return max1*max2, max1*min1
```
This function initializes two variables max1 and max2 to keep track of the two maximum numbers in the array, and two variables min1 and min2 to keep track of the two minimum numbers. It then iterates over the array, updating these variables as necessary. Finally, it returns the product of the two maximum numbers, and the product of the two maximum numbers and the smallest number. 

This solution assumes that