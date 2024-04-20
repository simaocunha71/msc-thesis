"""
Write a function to find whether a given array of integers contains any duplicate element.
assert test_duplicate(([1,2,3,4,5]))==False
"""
class Solution(object):
    def isDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        1. 找出大小相同的一组。
        2. 按照递增次序排列，再把这些值进行取和。
        3. 对于不重复的情况，取和为0；
                       else(有重复数)：取和>0
        """
        res = []
        # 按照递增次序排列
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in res:
                print("有重复数")
                return True
            else:
                res.append(nums[i])
        return False
        

if __name__=="__main__":
    sol = Solution()
    print(sol.isDuplicate([1,2,3,4]))
