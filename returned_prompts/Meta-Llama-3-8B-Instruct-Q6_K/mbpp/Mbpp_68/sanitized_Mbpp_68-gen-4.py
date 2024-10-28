def is_Monotonic(array):
  return array == array.sort() or array == array.sort()[::-1]
  # or
  # return array == sorted(array) or array == sorted(array, reverse=True)  # Python >= 3.7