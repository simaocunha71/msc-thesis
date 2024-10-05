    def check(nums):
        n = len(nums)
        for i in range(n):
            if nums[i] < nums[i - 1]:
                return False
        return True

    def move_one(nums):
        temp = nums.pop()
        nums.insert(0, temp)
        return nums

    def move_left(nums):
        return [nums[-1]] + nums[:-1]

    def move_right(nums):
        return nums[1:] + [nums[0]]

    if len(arr) == 0:
        return True

    temp = arr.copy()
    if check(temp):
        return True

    for i in range(len(arr)):
        temp = arr.copy()
        temp = move_one(temp)
        if check(temp):
            return True
        temp = arr.copy()
        temp = move_left(temp)
        if check(temp):
            return True
        temp = arr.copy()
        temp = move_right(temp)
        if check(temp):
            return True

    return False


