"""
Write a function to find the area of a rectangle.
assert rectangle_area(10,20)==200
"""
class Solution:
    def rectangleArea(self, width: int, height: int):
        return self.calculateArea(width,height)+self.calculateArea(2*height,width)