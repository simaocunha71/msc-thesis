    def specialFilter(nums):
        count = 0
        for num in nums:
            if abs(num) > 10 and str(num)[0] % 2 != 0 and str(num)[-1] % 2 != 0:
                count += 1
        return count


