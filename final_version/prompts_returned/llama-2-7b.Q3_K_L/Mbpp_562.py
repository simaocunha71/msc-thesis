"""
Write a python function to find the length of the longest sublists.
assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
"""
class Solution(object):
    def Find_Max_Length(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_length = 0

        for i in range(1, len(nums)):
            if not i % 2 == 0:
                temp = []
                sublist = [nums[i]] + nums[:i] # remove nums[:i] from nums
                while sublist[-1] != -1 and (len(sublist) > max_length):
                    if len(temp) > max_length:
                        max_length = len(temp)
                    temp.append(sublist[-1])
                    sublist = [i] + sublist[1:] # remove nums[:i] from sublist and add 1 to i
                if (len(temp) > max_length):
                    max_length = len(temp)
        return max_length