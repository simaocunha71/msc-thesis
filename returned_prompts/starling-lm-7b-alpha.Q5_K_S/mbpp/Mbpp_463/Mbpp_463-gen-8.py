```
def max_subarray_product(nums):
    max_product = nums[0]
    min_product = nums[0]
    max_global = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        max_global = max(max_global, max_product)
    return max_global
```
    
This is the O(n) solution for maximum product subarray, it uses two variables max_product and min_product to track the maximum and minimum product of subarray ending at the current index. It initializes both to the first element of the array. Then, it goes through the array and for each element, if it is negative, it swaps the values of max_product and min_product. Then, it calculates the maximum product of the subarray ending at the current index, and updates max_global if the calculated maximum product is greater than max_global.


The time complexity of this solution is O(n) because it goes through the array only once. The space complexity is O(1) because it only uses a few variables to store the maximum product and minimum product of the subarray, and max_global to store the maximum product of the whole array.


To test the solution, you can use the assert statement to check if the maximum product of the subarray is correct. Here is an example:
```python
def test_max_subarray_product():
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
```
This test case checks if the maximum product of the subarray [1, -2, -3, 0, 7, -8, -2] is 112, which is the correct answer.


This is a basic implementation of the solution. It can be extended to handle more complex scenarios, such as handling empty arrays, arrays with only negative numbers, or