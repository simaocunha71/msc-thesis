"""
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
"""
import heapq
def largest_n(self,nums): # function definition
    if len(nums)>0:
        self.result=nums[-1]
    else:
        return None
    
    for i in range(len(nums)-2,-1,-1): # n-1 times in this way to avoid duplication of code
        if nums[i+1]>self.result:# we can write in a more efficient way by not using two for loopex:
            self.result=nums[i+1]
    return self.result
class Solution(object): # here is the solution to this question
    def largestN(self, nums):
        """
        :param nums: a list of integers
        :return: an integer representing the n largest numbers in the nums list returned in descending order
        """
        return heap_queue_largest(nums, n=1) # call our custom function to get solution
        