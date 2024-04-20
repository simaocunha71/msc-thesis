"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""
# Time Complexity: O(n)
def max_Abs_Diff (arr): 
    # Your code here
	max_abs = int()
	for i in arr:
		if abs(i-arr[0]) > max_abs:
			max_abs = abs(i - arr[0])
	return max_abs
arr= [2,1,5,3]
print(max_Abs_Diff (arr))
