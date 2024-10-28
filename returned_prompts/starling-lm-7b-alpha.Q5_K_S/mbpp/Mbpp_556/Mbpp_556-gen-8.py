
def find_Odd_Pair(nums: list, target: int) -> int:
    def count(nums: list, target: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] ^ nums[j] == target:
                    res += 1
        return res
    return count(nums, target)


