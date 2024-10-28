```
def find_min_diff(arr, n): 
  
    # Sort the array
    arr.sort()
  
    # Initialize result
    min_diff = arr[1] - arr[0]
  
    # loop through the array
    for i in range(1, n):
        diff = arr[i] - arr[i - 1]
  
        # Update result if diff is less than min_diff
        if diff < min_diff:
            min_diff = diff
  
    return min_diff
```
