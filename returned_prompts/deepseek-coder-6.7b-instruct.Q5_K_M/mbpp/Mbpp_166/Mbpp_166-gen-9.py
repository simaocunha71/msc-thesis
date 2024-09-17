
def find_even_pair(lst):
  n = len(lst)
  count = 0
  for i in range(0, 32):
    cnt = 0
    for j in range(0, n):
      if((lst[j] & (1 << i))):
        cnt += 1
    count += cnt * (n - cnt) * 2
  return count


