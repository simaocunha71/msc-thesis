"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""
class Solution:
    def findMinProduct(self, nums):
        if not nums: return ''
        
        # sort the list
        self.nums = sorted(list(nums))
        
        count = len(self.nums) - 1
        for i in range(count):
            num_product= 1
            
            min_value = self.nums[i]
            for j in range(i+1,count):
                if j < count and self.nums[j] <= min_value:
                    break
            
                else:
                    num_product *= self.nums[j]
                    
            print("min num :", num_product)
        
        return min(num_product for num_product in range(1, count))