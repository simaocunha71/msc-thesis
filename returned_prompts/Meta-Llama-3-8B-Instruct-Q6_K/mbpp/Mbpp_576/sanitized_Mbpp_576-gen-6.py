def is_Sub_Array(big_array, small_array):
  if len(small_array) > len(big_array):
    return False
  for i in range(len(big_array) - len(small_array) + 1):
    if big_array[i:i+len(small_array)] == small_array:
      return True
  return False