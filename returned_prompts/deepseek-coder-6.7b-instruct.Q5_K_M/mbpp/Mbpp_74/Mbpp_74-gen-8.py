
def is_samepatterns(arr1, arr2):
  return len(set(zip(arr1, arr2))) == len(arr1)


