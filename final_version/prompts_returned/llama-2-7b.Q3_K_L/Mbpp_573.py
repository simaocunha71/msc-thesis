"""
Write a python function to calculate the product of the unique numbers in a given list.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
"""
class Solution:
    def uniqueProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        if len(nums) == 1: # base case for recursion!
            return 1
        
        
        product = 1
        sum_of_list = 0
        
        # sum the unique elements in list
        for x in nums:
            sum_of_list += x
            
        # if there are any negative number in sum_of_list, then the last element is negative. This condition can be used to identify the first negative integer.
        if sum_of_list < 0 and len(nums) == 1:
            return -1
        
        for x in nums[1:]: # start from second element
            
            product *= x
            
            # if nums.index(x) == 0, then the first element is not an unique element!
            if nums.index(x) == 0 or sum_of_list - len(nums[1:]) < 0:
                product = 0