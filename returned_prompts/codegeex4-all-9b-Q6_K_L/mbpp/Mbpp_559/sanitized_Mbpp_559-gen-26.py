def max_sub_array_sum(test_list: list,n: int) -> int:
  max_sum = 0
  for i in range(n):
    temp_sum = 0
    for j in range(i, n):
      temp_sum += test_list[j]
      max_sum = max(max_sum, temp_sum)
  return max_sum