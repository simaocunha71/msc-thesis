"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""
class Solution:
    def isSubarray(self, nums, target):
        n = len(target)
        
        def helper(i, j=0, acc=[1]):
            if i > n-j: return [acc[-1]] + [0]*n
            if i==n-j and all([t in a[0] for t in target]):
                return helper(i+1)
            if all([t in nums[i] for t in target]):
                acc.append(1)
            else:
                return helper(i+1, j + 1, acc[-1]+[0]*n)
            
        return helper(-1, 0)
        
sol = Solution()
print sol.isSubarray([2,4,3,5,7],[3,7])==False #True
