
def is_Sub_Array(list1: list, list2: list) -> bool:
  for i in range(len(list1)):
    if len(list1[i:]) >= len(list2) and list1[i:][:len(list2)] == list2:
      return True
  return False


