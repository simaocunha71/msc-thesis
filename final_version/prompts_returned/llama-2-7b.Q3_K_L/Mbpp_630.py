"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""
class Solution:
    def getAdjacentCoordinates(self, coordinate):
        # write your code here

def main():
    solution = Solution()
    print (solution.getAdjacentCoordinates((3, 2)))
    print (solution.getAdjacentCoordinates((4, 5)))
if __name__ == "__main__":
    main()