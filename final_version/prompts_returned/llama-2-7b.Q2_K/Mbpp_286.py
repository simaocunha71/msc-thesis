"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""

def findMaxSubArraySumRepeated(arr, N, step):
    if len(arr) < (N-step+1)*step: return []

    # find the largest sum in the original array
    max_sum = -1
    for i in range(0, len(arr), step):
        max_sum += arr[i]
    
    # find the largest sum of a sub-array which has length = (N-step+1)*step and contains only one element is i.e. [arr[i], .., arr[i]]
    for n in range(0, len(max_sum), step):
        if max_sum > 0: 
            if max_sum >= 0:
                # find the largest sum of a sub-array which has length (N+1)*step and contains only one element is i.e. [arr[i], .., arr[i] + max(max_sum) * step - 1]
                
                max_sub_sum = max(int(max(arr[i:i+n]), 0), 
                                   int(-3*max_sum), -1)
                if max_sub_sum >= 0:
                    return [arr[i]] + [max_sub_sum] * (step-1), max_sum, 0
        # else:
            continue
    
    for n in range(0, len(max_sum), step):
        if max_sum >= 0:
            if max_sum >= 0:
                # find the largest sum of a sub-array which has length (N+1)*step and contains only one element is i.e. [arr[i], .., arr[i] + max(max_sum) * step - 1]
                    
                max_sub_sum = max(int(max(arr[i:n+m])), 
                                    int(-3*max_sum), -1)
                if max_sub_sum >= 0:
                    return [arr[i]], max_sum, n, step
            continue
    
    for n in range(0, len(max_sum), step):
        # find the largest sum of a sub-array which