```
def max_Product(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    res = ()
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
        if i < min1:
            min2 = min1
            min1 = i
        elif i < min2:
            min2 = i
    return (max1, max2) if max1*max2 > max1*min1 and max1*max2 > max2*min2 else (min1, min2)
```
This function first finds the two maximum and two minimum values in the array. It then returns the pair with the highest product, which is either the pair of maximum values or the pair of minimum values, depending on which one has the highest product. The unit test `assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)` helps to clarify the problem by showing that the function should return the pair with the highest product, not just the maximum value. 





This function works by iterating over the array and keeping track of the maximum and minimum values. It then returns the pair with the highest product, which is either the pair of maximum values or the pair of minimum values, depending on which one has the highest product. The time complexity is O(n), where n is the length of the array, and the space complexity is O(1), as it only uses a constant amount of space to store the maximum and minimum values.