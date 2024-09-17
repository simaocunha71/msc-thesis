
def get_median(a, b, n):
  merged_list = sorted(a + b)
  return (merged_list[n-1] + merged_list[n]) / 2.0


