    def count_odd(nums):
        odd_count = 0
        for num in nums:
            if num % 2 != 0:
                odd_count += 1
        return odd_count

    def make_even(nums):
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                nums[i] += 1

    # Count the odd elements
    odd_count = count_odd(arr)
    if odd_count == 0:
        return 0

    # Change odd elements to even
    make_even(arr)

    # Count the odd elements again
    odd_count_after_change = count_odd(arr)

    return odd_count - odd_count_after_change


