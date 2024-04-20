"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""
class Solution:
    def centeredHexagonalNumber(self, n):
        return self.iterative([], 1, n)

    def iterative(self, hexagonal_series, index, sum):
        if index > len(hexagonal_series)-2:
            return None
        if index == len(hexagonal_series)-3:
            return index * sum
        temp = self.iterative(hexagonal_series[index-1], index+1, sum + hexagonal_series[index])
        if temp is not None:
            return temp
    