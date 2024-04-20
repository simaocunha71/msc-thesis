"""
Write a function to find the lateral surface area of a cube given its side length.
assert lateralsurface_cube(5)==100
"""
class Solution:
    def lateralSurfaceArea(self, n):
        sum = n*n
        ans = 3 * (sum + int((1/2)*np.sqrt(sum)))
        return ans
