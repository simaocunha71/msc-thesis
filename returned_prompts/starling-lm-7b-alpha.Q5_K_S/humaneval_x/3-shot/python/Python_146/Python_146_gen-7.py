    def specialFilter(nums):
        counter = 0
        for i in range(len(nums)):
            if (nums[i] > 10) and (nums[i] % 2 != 0) and (int(str(nums[i])[0]) % 2 != 0) and (int(str(nums[i])[-1]) % 2 != 0):
                counter += 1
        return counter


