
def count_binary_seq(n):
  count = 0
  for i in range(n+1):
    count += 2**i
  return count


