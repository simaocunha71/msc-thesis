def max_Abs_Diff(arr):
    return max(abs(a-b) for a, b in zip(arr, arr[1:]))

print(max_Abs_Diff((2,1,5,3))) # 4

# 2nd solution
def max_Abs_Diff(arr):
    min_val = min(arr)
    max_val = max(arr)
    return max_val - min_val

print(max_Abs_Diff((2,1,5,3))) # 4

# 3rd solution
def max_Abs_Diff(arr):
    return max([abs(a-b) for a in arr for b in arr if a != b])

print(max_Abs_Diff((2,1,5,3))) # 4

# 4th solution
def max_Abs_Diff(arr):
    return max(j-i for i, j in combinations(sorted(arr), 2))

print(max_Abs_Diff((2,1,5,3))) # 4
<jupyter_output>
4
<jupyter_text>
**Question 2:**Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.Solution: This problem can be solved by using the concept of prefix and suffix products. The prefix product of an array at index i is the product of all the numbers before i and the suffix product is the product of all the numbers after i. We can get the result by multiplying the prefix and suffix products.
<jupyter_code>
# Python code to solve the problem
def product_except_self(nums):
    # Length of the input array
    n = len(nums)
    
    # The left and right arrays as described in the algorithm
    left, right = [0]*n, [0]*n
    
    # Final answer array
    answer = [0]*n
    
    # Left[i] contains the product of all the numbers to the left of i
    left[0] = 1
    for i in range(1, n):
