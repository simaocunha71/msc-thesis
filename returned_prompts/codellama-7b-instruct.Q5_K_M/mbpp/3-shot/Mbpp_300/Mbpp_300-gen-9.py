
def count_binary_seq(n: int) -> float:
  count = 0
  for i in range(2**n):
    bin_seq = bin(i)
    if bin_seq.count('1') == bin_seq.count('0'):
      count += 1
  return count


