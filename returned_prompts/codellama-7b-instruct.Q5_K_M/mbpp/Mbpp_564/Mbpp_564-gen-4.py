
def count_Pairs(myList: list, n: int) -> int:
  count = 0
  for i in range(1, n):
    for j in range(i+1, n):
      if myList[i] != myList[j]:
        count += 1
  return count


