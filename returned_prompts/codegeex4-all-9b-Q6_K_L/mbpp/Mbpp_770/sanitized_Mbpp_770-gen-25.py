def odd_num_sum(n):
  odd_nums = [i for i in range(1, 2*n+1, 2)]
  return sum([i**4 for i in odd_nums])