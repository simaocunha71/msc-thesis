```
def max_Product(arr):
    if len(arr) < 2:
        return None
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x
        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2:
            min2 = x
    return max1 * max2 if max1 * max2 > min1 * min2 else (min1, min2)
```   


Explanation:
The function first checks if the array has less than 2 elements. If it does, it returns None. 

Then it initializes two variables max1 and max2 to negative infinity, and two variables min1 and min2 to positive infinity. 

It then iterates over each element in the array. If the current element is greater than max1, it updates max2 to be max1 and max1 to be the current element. If the current element is greater than max2 but not max1, it updates max2 to be the current element. 

It does the same for min1 and min2, but for smaller numbers.

Finally, it returns the product of max1 and max2 if it's greater than the product of min1 and min2, otherwise it returns the pair of min1 and min2. This is because the maximum product can either be the product of the two largest numbers, or the product of the two smallest numbers (in absolute value). 

This solution has a time complexity of O(n), where n is the number of elements in the array. This is because it makes a single pass over the array. The space complexity is O(1), which means the space required does not change with the size of the input array, so it is constant.   


The unit test `assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)` checks if the function correctly returns the pair with the highest product from the given array.   


The function can also be implemented using the built-in max function with a key function that returns the absolute value of the number, and the built-in min function. This would make the code more concise but less efficient.   


Here is the concise version:

```
def max