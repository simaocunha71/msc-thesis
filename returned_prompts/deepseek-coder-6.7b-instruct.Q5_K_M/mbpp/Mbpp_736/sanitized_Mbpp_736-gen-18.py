import bisect
def left_insertion(a, x):
  return bisect.bisect_left(a, x)