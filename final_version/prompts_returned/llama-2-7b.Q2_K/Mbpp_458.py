"""
Write a function to find the area of a rectangle.
assert rectangle_area(10,20)==200
"""
class Solution:
    def rectangleArea(self,l,b):
        if (l*b)>=0 and l>=1 and b>=1: 
            return l*b    
        else:
            raise Exception("Please enter the length and breadth of the rectangle")     