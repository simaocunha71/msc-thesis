```
def max_Product(nums):
    if not nums:
        return None
    max1 = max2 = float('-inf')
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return (max1, max2)
```
This function first checks if the input array is empty. If it is, it returns None. Then it initializes two variables, max1 and max2, to negative infinity. It then iterates over the array, updating max1 and max2 whenever it finds a number that is greater than the current max1 or max2. Finally, it returns a tuple containing max1 and max2, which are the two numbers with the highest product. 

The unit test `assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)` indicates that the function should return the pair with the highest product, not the pair with the highest sum. This is why we don't simply return the sum of max1 and max2. 

The time complexity of this function is O(n), where n is the number of elements in the input array. This is because it iterates over the array once. The space complexity is O(1), which means it uses constant space. This is because it uses a fixed amount of space to store the variables max1, max2, and the input array. 

Note: This function assumes that the input array is not empty and contains at least two distinct elements. If the input array can be empty or contain less than two distinct elements, additional error checking code would be needed.  For example, we could add a check at the beginning of the function to return None if the array is empty or has less than two elements.  We could also add a check to ensure that max1 and max2 are not the same element, in case the array contains duplicate elements.   However, without this additional error checking code, the function will fail if the input array is empty or contains less than two distinct elements.  For example, if the input array is [1], the function will return (1, 1) instead of None.  If the input array is [1, 1], the function will return (1, 1) instead of None.  If the input array is [1], the function will return (1, -inf) instead