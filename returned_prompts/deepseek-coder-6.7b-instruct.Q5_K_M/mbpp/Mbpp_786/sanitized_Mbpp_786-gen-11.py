import bisect
def right_insertion(arr, val):
  return bisect.bisect_right(arr, val)