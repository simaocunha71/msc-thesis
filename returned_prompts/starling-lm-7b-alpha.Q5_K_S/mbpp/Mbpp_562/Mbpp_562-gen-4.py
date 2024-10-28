
def Find_Max_Length(list1: list) -> int:
  max_length = 0
  for i in range(len(list1)):
    temp = 0
    for j in range(i,len(list1)):
      temp += 1
      if temp > max_length:
        max_length = temp
  return max_length


