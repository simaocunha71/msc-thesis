
def get_pairs_count(arr, sum): 
  n = len(arr) 
  m = [0] * 1000
  twosum_count = 0
  for i in range(0, n): 
    twosum_count += m[sum - arr[i]] 
    for j in range(0, i): 
      if (arr[i] == arr[j]): 
        m[arr[i] + arr[j]] += 1
  return twosum_count 


