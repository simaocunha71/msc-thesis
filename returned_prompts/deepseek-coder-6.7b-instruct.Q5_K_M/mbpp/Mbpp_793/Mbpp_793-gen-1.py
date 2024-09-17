
def last(arr, target):
  return len(arr) - 1 - arr[::-1].index(target)


