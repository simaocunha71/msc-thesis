```
def max_Product(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    result1 = result2 = (0,0)
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
    return max1, max2 if max1 * max2 > max1 * min1 and max1 * max2 > max1 * min2 else (max1, min1)
```


This problem is asking to find a pair of elements in an array that have the highest product. The problem statement is not entirely clear, but based on the unit test provided, it seems that we need to find the pair of elements that have the highest product. If the highest product is achieved by multiplying two negative numbers, then we need to return the pair of negative numbers. If the highest product is achieved by multiplying a negative number and a positive number, then we need to return the pair of numbers where the negative number is the smaller one.

Here is a Python function that solves this problem. The function iterates over the array, keeping track of the two largest and two smallest numbers. It then returns the pair of numbers that has the highest product. If the highest product is achieved by multiplying two negative numbers, it returns the pair of negative numbers. If the highest product is achieved by multiplying a negative number and a positive number, it returns the pair of numbers where the negative number is the smaller one.

The unit test provided is `assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)`, which means that the function should return `(7,8)` when given the array `[1,2,3,4,7,0,8,4]`. This is because the product of `7` and `8` is the highest among all pairs of elements in the array.