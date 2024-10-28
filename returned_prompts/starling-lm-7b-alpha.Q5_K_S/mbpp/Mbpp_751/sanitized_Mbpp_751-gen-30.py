def check_min_heap(test_list: list) -> bool:
  if len(test_list) == 0:
    return True
  for i in range(len(test_list)//2):
    if test_list[i] > test_list[2*i+1] and test_list[i] > test_list[2*i+2]:
      return False
  return True