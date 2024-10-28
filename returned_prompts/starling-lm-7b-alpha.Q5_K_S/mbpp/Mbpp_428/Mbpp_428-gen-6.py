
def shell_sort(test_list):
  n = len(test_list)
  gap = n//2
  while gap > 0:
    for i in range(gap, n):
      temp = test_list[i]
      j = i
      while j >= gap and test_list[j-gap] > temp:
        test_list[j] = test_list[j-gap]
        j -= gap
      test_list[j] = temp
    gap //= 2
  return test_list


