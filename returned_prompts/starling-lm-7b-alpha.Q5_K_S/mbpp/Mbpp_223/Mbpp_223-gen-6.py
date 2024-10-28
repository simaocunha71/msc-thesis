
def is_majority(sorted_list:list, n:int, element:int) -> bool:
  count = 0
  for i in range(0, n):
    if sorted_list[i] == element:
      count += 1
      if count > n//2:
        return True
  return False


