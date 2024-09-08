def find_min_diff(arr, n):
    # sort the array
    arr = sorted(arr)
    
    # initialize the minimum difference
    min_diff = float('inf')
    
    # find the minimum difference
    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        min_diff = min(min_diff, diff)
    
    return min_diff

# test the function
print(find_min_diff((1,5,3,19,18,25),6)) # should return 1

"""
Explanation:
The given array is [1, 5, 3, 19, 18, 25]. After sorting the array, it becomes [1, 3, 5, 18, 19, 25]. 
The minimum difference between any two elements can be found by checking the difference between consecutive elements. 
The minimum difference in this case is 1.
"""
<jupyter_output>
1
<jupyter_text>
Question 2:Given an array of integers, find the maximum sum of a subsequence with the constraint that no two elements in the chosen numbers in the sequence should be adjacent in the array.
<jupyter_code>
