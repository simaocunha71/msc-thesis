    def sum_of_digits(x):
        return sum(map(int, str(x)))

    sorted_nums = sorted(nums, key=sum_of_digits)
    for i in range(len(nums)):
        sorted_nums[i] = (nums.index(sorted_nums[i]), sorted_nums[i])

    return [x[1] for x in sorted(sorted_nums)]


