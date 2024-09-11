```
def max_product(nums):
    def max_subseq(nums, left, right):
        max_right = [0] * len(nums)
        max_right[right] = nums[right]
        max_prod = [1] * len(nums)
        for i in xrange(right - 1, left - 1, -1):
            max_right[i] = max(nums[i], max_right[i + 1] * nums[i])
            max_prod[i] = max(max_prod[i + 1] * nums[i], nums[i])
        return max_right[left], max_prod[left]

    max_left, max_prod_left = max_product(nums[:len(nums) / 2])
    max_right, max_prod_right = max_product(nums[len(nums) / 2:])
    return max(max_left * max_right, max_left, max_right, max_prod_left * max_prod_right)
```

Explanation:
To solve the problem, we can divide the array into two parts and find the maximum product of increasing subsequences in each part. Then, we can find the maximum product among the products of the two parts, the product of the increasing subsequence in the left part, and the product of the increasing subsequence in the right part.

In the `max_product` function, we first find the maximum product of increasing subsequences in the left and right parts of the array. We do this by recursively calling the `max_product` function on the left and right parts of the array. Then, we find the maximum product among the products of the two parts, the product of the increasing subsequence in the left part, and the product of the increasing subsequence in the right part.

In the `max_subseq` function, we find the maximum product of an increasing subsequence in the given range. We initialize the `max_right` array with all zeros. Then, we iterate through the range from right to left. For each number, we update the `max_right` array by taking the maximum between the current number and the product of the current