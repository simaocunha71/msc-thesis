"""
In this problem we have to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.

Let's break down the problem and solve it step by step:

Step 1: Define a function max_product that takes an array as an input.

Step 2: Initialize a variable max_product to 1. This will help us store the maximum product formed by multiplying the numbers of an increasing subsequence.

Step 3: Initialize two pointers, left and right, to 0 and len(nums)-1, respectively. These pointers will help us traverse the array from both ends.

Step 4: Use a while loop to traverse the array until left < right. This is because if we traverse the array until left <= right, we might skip the maximum increasing subsequence if it is present at the end of the array.

Step 5: Inside the while loop, check if the number at the left pointer is less than the number at the right pointer. If it is, update the max_product by multiplying it with the number at the left pointer and increment the left pointer by 1.

Step 6: If the number at the left pointer is not less than the number at the right pointer, update the max_product by multiplying it with the number at the right pointer and decrement the right pointer by 1. This is because we need to consider the increasing subsequences from both ends of the array.

Step 7: After traversing the entire array, return the max_product.

Here's the code for the max_product function:
"""

def max_product(nums):
    max_product = 1
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] < nums[right]:
            max_product *= nums[left]
            left += 1
        else:
            max_product *= nums[right]
            right -= 1

    return max_product

# Test the function with the given example
assert max_product([3, 100, 4, 5, 150, 6]) == 3000

# Test the function with different inputs
assert max_