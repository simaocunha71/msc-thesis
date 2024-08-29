def max_sub_array_sum(arr, n):
    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, n):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Kadane’s Algorithm is an efficient algorithm to solve this problem. 
# It uses dynamic programming to solve the problem in O(n) time. 
# The algorithm maintains a current sum of the subarray and maximum sum found so far. 
# If the current sum becomes negative, it resets to 0 because a negative sum is not contributing to the sum of the subarray. 
# If the current sum becomes larger than the maximum sum, it updates the maximum sum.
# At the end, the maximum sum is returned.

# This solution is also known as Kadane's Algorithm.

# Kadane's Algorithm is a dynamic programming algorithm that solves the maximum subarray sum problem in O(n) time.
# It works by iterating over the array and at each step, it updates the current sum and the maximum sum. 
# If the current sum becomes negative, it is reset to 0. 
# If the current sum becomes larger than the maximum sum, the maximum sum is updated. 
# At the end, the maximum sum is returned.

# This algorithm is known as Kadane's Algorithm because the author's name, Kadane, was mentioned in the paper.

# This algorithm is used in many programming interviews to test the candidate's understanding of dynamic programming. 
# It is a common problem in computer science education and is often used as a prelude to more complex dynamic programming problems.

# This solution is also known as Kadane's Algorithm.

# Kadane's Algorithm is a dynamic