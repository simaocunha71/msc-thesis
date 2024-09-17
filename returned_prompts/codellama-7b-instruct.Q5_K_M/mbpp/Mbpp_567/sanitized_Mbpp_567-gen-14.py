def issort_list(my_list: list) -> bool:
  for i in range(len(my_list)-1):
    if my_list[i]>my_list[i+1]:
      return False
  return True