import bisect
def left_insertion(arr,val):
  return bisect.bisect_left(arr,val)