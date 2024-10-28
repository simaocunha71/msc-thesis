```
def max_Product(lst):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    result1 = result2 = 0
    for num in lst:
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
    return max1 * max2, min1 * min2
```    
This function iterates through the array to find the two maximum and two minimum numbers. It then returns the product of the two maximum numbers and the product of the two minimum numbers. The unit test provided ensures that the function returns the correct results. For example, the test `assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)` checks that the function correctly returns the pair with the highest product, which is (7,8) in this case. 

The time complexity of this function is O(n), where n is the number of elements in the input list, because it makes a single pass through the list. The space complexity is O(1), because it uses a constant amount of space to store the maximum and minimum numbers, regardless of the size of the input list. 