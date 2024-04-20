"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""
import heapq
def largest_n(nums, n):
	if len(nums) < n:
		return None
	else:
		size = heapq.nlargest(n - 1, nums)
		for i in range(0,len(size)):
			print (i+1, size[i])


"""
The max function returns the largest element of a list.
max_n = lambda nums: heapq.nlargest(2,nums)
assert set([79, 80, 81]).issubset(set(larg_nnum([45, 60, 50, 39, 40, 50],2)))
"""