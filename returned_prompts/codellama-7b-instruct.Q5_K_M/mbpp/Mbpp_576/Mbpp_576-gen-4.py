
def is_Sub_Array(main_array: list, sub_array: list) -> bool:
  if not sub_array:
    return True
  for i in range(len(main_array)):
    if main_array[i:i+len(sub_array)] == sub_array:
      return True
  return False


