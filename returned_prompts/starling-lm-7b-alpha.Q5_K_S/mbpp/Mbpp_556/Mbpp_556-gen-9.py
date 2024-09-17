
def find_Odd_Pair(nums: list, target: int) -> int:
    def check(nums):
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] ^ nums[j]) & 1:
                    res += 1
        return res
    return check(nums)


