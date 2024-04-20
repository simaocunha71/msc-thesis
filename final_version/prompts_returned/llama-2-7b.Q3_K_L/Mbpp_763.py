"""
Write a python function to find the minimum difference between any two elements in a given array. 
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""
# Time Complexity: O(n)
def find_min_diff(a): #time complexity is O(n) which is the number of elements.
    return min(sorted(set(a))-set([min(a)]))
    
print("find_min_diff((1,5,3,19,18,25),6) ", find_min_diff((1,5,3,19,18,25), 6) )
