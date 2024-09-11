from typing import List

def find_min_diff(nums: List[int], target: int) -> int:
    nums.sort()
    min_difference = float('inf')
    for i in range(len(nums)):
        if target == nums[i]:
            min_difference = 0
            break
        diff = target - nums[i]
        if diff < min_difference:
            min_difference = diff
    return min_difference

if __name__ == '__main__':
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    print('All tests passed')







"""
In this program, we define a function find_min_diff that takes two parameters:
    - nums: a list of integers
    - target: an integer
The function first sorts the list nums in ascending order using the sort method.
Then, it initializes a variable min_difference with a value of positive infinity (float('inf')).
The function then iterates through the sorted list nums using a for loop and checks if the target value is equal to any of the elements in the list. If it is, the min_difference is set to 0 and the loop is broken.
Otherwise, the function calculates the difference between the target and the current element in the list, and checks if it is smaller than the current min_difference. If it is, the min_difference is updated with the new smaller value.
Finally, the function returns the min_difference, which represents the minimum difference between any two elements in the given array.

"""


# Python3 program to find minimum difference
# between any two elements in a given array

# Function to find minimum difference
def find_min_diff(nums, target):
    nums.sort()
    min_difference = float('inf')
    for i in range(len(nums)):
        if target == nums[i]:
            min_difference = 0
            break
        diff = target - nums[i]
        if diff < min_difference:
            min_difference = diff
   