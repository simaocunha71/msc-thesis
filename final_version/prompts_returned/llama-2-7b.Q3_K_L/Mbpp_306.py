"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""
def max_sum_increasing_subseq(arr, i, j, k=None):
    if k is None: return arr[i] # no element to be considered hence sum will be the same as first value of array
    
    max_sum = arr[0] + 1
    idx = -1

    for idx in range(len(arr)):
        if i == len(arr): break # last iteration reached, so no need to go further
        
        if not isIncreasingSubseq(arr[idx], arr[i+1:j], k=k): continue
        else:
            current_sum = max_sum + arr[i]
            
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum
# Time and Space Complexity O(n) for loop
# O(n^2 - nlog(n)) as worst case scenario (no element to consider, so last element of array will be considered)        
