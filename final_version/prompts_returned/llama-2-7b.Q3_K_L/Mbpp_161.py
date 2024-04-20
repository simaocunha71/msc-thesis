"""
Write a function to remove all elements from a given list present in another list.
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
"""
class Solution:
    def removeElements(self, nums: List[int], target: List[int]) -> List[int]:
        new_list = []
        j = i = 0
        while len(nums) > 0 or j < len(target):
            if (j >= len(target)) and len(nums) == 0: break
            if nums[-1] == target[j]: nums.pop()
            new_list.append(nums[-1])
            j += 1
        return new_list