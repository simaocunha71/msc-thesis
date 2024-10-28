def get_median(arr1, arr2, size):
  merged_arr = sorted(arr1 + arr2)
  median = (merged_arr[size//2] + merged_arr[(size-1)//2]) / 2
  return median

