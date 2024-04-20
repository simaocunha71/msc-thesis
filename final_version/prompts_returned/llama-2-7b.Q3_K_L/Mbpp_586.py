"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""
class Solution:
    def split(self, nums: List[int], n: int) -> None:
        """Given a sorted array of numbers and an index (starting from 0) return a list of the values at indices [0, n-1] and [n]."""
        if not isinstance(nums, list): nums = [nums]
        
        length = len(nums)

        # check if n is less than zero or greater than 5 then return
        if (n < 0) or (n > 4):
            return []

        # return the values at indices [0, n-1] and [n] when length is even
        if(length % 2 == 0):
            return self.split_even(nums, n)
        
        # return the values at indices [0, n] when the length is odd
        else:
            return self.split_odd(nums, n)
    
    def split_even(self, nums: List[int], n: int)->List[int]:
        """When the length of array is even"""
        # split and create two lists to hold the values of indices [0...n-1] and [n+1...length]"""        
        # create a list and populate it with the first list
        split_list = []
        
        for i in range(n, length): # n > 0 then loop between n and length
            split_list.append(nums[i])            
                    
        # merge the two lists together, add the first part to the end
        new_list = [split_list[0], *split_list[1:]]
        
        return new_list
    
    def split_odd(self, nums: List[int], n: int)->List[int]:
        """When the length of array is odd"""
        # split and create two lists to hold the values of indices [0...n-1] and [n+1...]"""
        # create a list and populate it with the first list
        
        if(length % 2 == 1):
            split_list = []
            
            for i in range(n, length):
               