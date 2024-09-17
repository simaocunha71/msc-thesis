from collections import Counter
def get_pairs_count(arr, sum):
  n = len(arr)
  m = Counter(arr)
  twice_count = 0
  for i in range(0, n):
    twice_count += m[sum - arr[i]]
    if (sum - arr[i] == arr[i]):
      twice_count -= 1
  return int(twice_count / 2)