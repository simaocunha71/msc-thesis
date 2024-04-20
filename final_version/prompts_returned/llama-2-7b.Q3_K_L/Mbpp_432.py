"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""
class Solution:
    def median_trapezium(self, left: int, right: int, target:int) -> int:
        # Write your solution here
        if(left >= 1 and target < right):
            return target
        
        if (right - left <=2):
            
            return (min((target,right+1),max((left-1,target))) - max((target,left-1)) + min((left-1,target)),))//2
        else:
            return(int(median_trapezium(left-1, target-1, right) + median_trapezium(left+1, target-1, right)))//2
        
#print(median_trapezium(15, 25, 35))   # Test your code