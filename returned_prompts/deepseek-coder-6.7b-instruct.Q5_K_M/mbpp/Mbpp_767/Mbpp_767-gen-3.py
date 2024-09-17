
def get_pairs_count(arr, sum):
  n = len(arr)
  m = [0] * 1000
  twosum = [0] * 1000
  for i in range(0, n):
    temp = arr[i] % 1000
    twosum[ (sum-arr[i]) % 1000] += 1
    m[temp] += 1
  twice_count = 0
  for i in range(0, n):
    temp = arr[i] % 1000
    if (3000 - arr[i]) % 1000 < temp:
      twice_count += (m[temp] * (m[temp]-1) // 2 - 1)
    else:
      twice_count += (m[temp] * twosum[(3000-arr[i]) % 1000])
  return twice_count


