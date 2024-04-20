"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
class Solution:
    def findMax(self, nums):
        n = len(nums) - 1   # the length of the list is -1
        maxCount = []       # the largest digit number in the list
        
        for i in range(n):      # iterate over each character
            count = [0] * (i+1)     # create a new array to store the counts
            
            # store the last character count 
            count[i] = nums[-1 - n]
            
            for j in range(n-i, n):      # iterate over each of the digits left to right
                if (count[j] == 0) and (nums[j+i] != 0):    # if the digit count is zero in the character, then it must be nonzero.
                    count[j] = nums[j + i]        # store the last non-zero digit to a new array as its own character count
                else:   # otherwise check the next previous position for this digit
                    if (count[i] != 0) and (nums[i] == nums[j + i]):     # if there is no zero in the last character, find out which of the two digits to use
                        count[i+1] = max(count[i+1], count[i])          # store the largest digit number
                        
            maxCount.append(max(count))  # store the largest digit number for each character in a new list as the maximum value of its own corresponding counts array
            
        return max(maxCount)  # finally return the maximum value of this maxCount list
```