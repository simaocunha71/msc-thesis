"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""
class Solution:
    def findMaxProduct(self, nums):
        if not nums: return False
        
        # sort the list
        l = sorted(nums, key=lambda x:x[1])
        n = len(l)
        
        # check if we have a product of 0
        count_zero = 0
        for i in range(n):
            if l[i][1] == 0:
                count_zero += 1
            elif l[i][1] < 0:
                print('negative')
        
        # check if the list is empty
        if n == 0: return False
        
        # find the first element of the pair that is not equal to 0
        index = -1
        for i in range(n):
            if l[i][1] != 0 and len(nums) > 2:
                index += 1
                
                # return the absolute value of the product of the first element and the second last element
                # this is because we have to find one element that are equal to it's previous one and 
                # find it out
                return abs(max_product = l[index] * l[-1])
                
        return False