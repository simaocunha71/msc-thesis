
def odd_length_sum(arr):
  n = len(arr)
  ans = 0
  for i in range(n):
    ans += ((arr[i]*((i+1)*(n-i)//2 + 1))//2)
  return ans


