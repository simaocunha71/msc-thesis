def check_min_heap(test_list: list) -> bool:
  for i in range(len(test_list)//2):
    parent = i
    child = 2*parent+1
    if child >= len(test_list):
      break
    if test_list[parent] > test_list[child]:
      return False
    if child + 1 < len(test_list):
      if test_list[parent] > test_list[child+1]:
        return False
  return True