
def max_sub_array_sum_repeated(arr: list, k: int, n: int) -> int:
  max_sum = -999999999999
  for i in range(k):
    cur_sum = 0
    for j in range(n):
      cur_sum += arr[j]
      if cur_tmp > max_sum:
        max_sum = cur_sum
  return max_sum

