def get_pairs_count(arr, sum):
  n = len(arr)
  m = [0] * 1000
  twosum = [0] * 1000
  for i in range(0, n):
    temp = arr[i]
    for j in range(0, i):
      if (arr[j] + temp == sum):
        twosum[arr[j]] += 1
    m[temp] += 1
  count = 0
  for i in range(0, len(twosum)):
    if (twosum[i] > 0):
      count += (twosum[i] * m[i])
  return count