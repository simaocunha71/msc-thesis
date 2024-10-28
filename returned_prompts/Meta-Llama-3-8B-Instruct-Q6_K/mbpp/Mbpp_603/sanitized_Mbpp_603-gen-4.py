def get_ludic(n):
  lucid_nums = [i for i in range(1, n+1) if len(str(i)) == len(str(2*i)) == len(str(3*i)) and str(i) == str(2*i) == str(3*i)]
  return lucid_nums