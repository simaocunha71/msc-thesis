def find_min_diff(arr, n):
    arr.sort()
    min_diff = float("inf")
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        min_diff = min(min_diff, diff)
    return min_diff

def test_find_min_diff():
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    assert find_min_diff((-1,2,1,0,3,4,5),7) == 1
    assert find_min_diff((-10,-1,0,1,2,3,4,5),8) == 1
    assert find_min_diff((1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000),8) == 1000
    assert find_min_diff((1,2,3,4,5,6,7,8),8) == 1
    print("All test cases passed.")

test_find_min_diff()

# Time complexity : O(nlogn)
# Space complexity : O(1)

"""
Explanation:
To solve this problem, we sort the array in ascending order. Then we compare each element with its adjacent element and keep track of the minimum difference.
The time complexity of the sorting operation is O(nlogn) because we use the built-in sort() function in Python, which has a time complexity of O(nlogn). The space complexity of the function is O(1) because we don't use any extra space that scales with the size of the input.
"""

"""
Test cases:

test_find_min_diff()
"""

# Python3 program to find the
# minimum difference between
# two elements in an array

# Function to find the minimum
# difference between two elements
# in an array
def find_min_diff(arr, n):
    # Sort the array
    arr.sort()

    # Initialize minimum difference
   