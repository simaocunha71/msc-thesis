
def count_binary_seq(n):
  count = 0
  for i in range(2**(2*n)):
    bin_num = bin(i)[2:].zfill(2*n)
    if sum(map(int, bin_num[:n])) == sum(map(int, bin_num[n:])):
      count += 1
  return count


