def get_pairs_count(arr, sum):
  n = len(arr)
  m = [0] * 1000
  two_sums = 0
  for i in range(0, n):
    if(arr[i] > sum // 2):
      two_sums += m[sum - arr[i]]
    m[arr[i]] += 1
  return two_sums