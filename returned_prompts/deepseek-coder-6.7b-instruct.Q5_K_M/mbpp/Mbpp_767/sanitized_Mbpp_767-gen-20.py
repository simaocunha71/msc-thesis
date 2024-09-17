def get_pairs_count(arr, sum):
  n = len(arr)
  m = [0] * 1000
  twoEleSum = [0] * 1000
  for i in range(0, n):
    temp = arr[i]
    twoEleSum[i] = arr[i]*2
    m[temp] += 1
  twice_count = 0
  for i in range(0, n):
    twice_count += m[sum - arr[i]]
    if (sum - arr[i] == arr[i]):
      twice_count -= 1
  return int(twice_count / 2)