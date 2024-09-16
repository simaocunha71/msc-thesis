
def max_sum(arr):
    return max(max_sum_helper(arr, True), max_sum_helper(arr, False))

def max_sum_helper(arr, increasing):
    if len(arr) == 1:
        return arr[0]

    max_sum = 0
    for i in range(len(arr)):
        if increasing:
            if i == 0 or arr[i] > arr[i-1]:
                max_sum = max(max_sum, max_sum_helper(arr[:i+1], True) + max_sum_helper(arr[i+1:], False))
        else:
            if i == 0 or arr[i] < arr[i-1]:
                max_sum = max(max_sum, max_sum_helper(arr[:i+1], True) + max_sum_helper(arr[i+1:], False))

    return max_sum
