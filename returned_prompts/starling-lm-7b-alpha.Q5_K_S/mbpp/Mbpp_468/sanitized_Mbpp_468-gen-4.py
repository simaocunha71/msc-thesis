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