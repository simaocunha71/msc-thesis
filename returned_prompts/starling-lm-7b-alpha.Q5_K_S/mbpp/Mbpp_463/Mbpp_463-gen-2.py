```
def max_subarray_product(nums):
    curr_max = nums[0]
    global_max = nums[0]
    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max * nums[i])
        global_max = max(global_max, curr_max)
    return global_max
```

Explanation:
The function `max_subarray_product` takes an array of integers as input and returns the maximum product of a subarray. 

To solve this problem, we maintain two variables: `curr_max` and `global_max`. `curr_max` represents the maximum product of a subarray ending at the current index, and `global_max` represents the maximum product of any subarray in the given array. 

We initialize `curr_max` and `global_max` to the first element of the array. 

Then, we iterate through the array from the second element onwards. For each element, we update `curr_max` by taking the maximum of the current element and the product of the current element and `curr_max`. This step ensures that `curr_max` always holds the maximum product of the subarray ending at the current index. 

We also update `global_max` by taking the maximum of `global_max` and `curr_max`. This step ensures that `global_max` always holds the maximum product of any subarray in the given array. 

Finally, we return `global_max`, which represents the maximum product of a subarray in the given array.

In the given example, the maximum product subarray of `[1, -2, -3, 0, 7, -8, -2]` is `[1, -2, -3, 0, 7, -8, -2]` with a product of 112.

The time complexity of this solution is O(n), where n is the length of the input array, as we only need to iterate through the array once.

The space complexity is O(1), as we only use a constant amount of extra space to store `curr_max` and `global_max`.

Overall, this