
def count_Pairs(test_list: list,n: int) -> int:
  counter = 0
  for i in range(len(test_list)):
    for j in range(i+1,len(test_list)):
      if test_list[i] != test_list[j]:
        counter += 1
  return counter


