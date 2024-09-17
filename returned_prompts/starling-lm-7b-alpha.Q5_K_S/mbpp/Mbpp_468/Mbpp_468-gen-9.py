
def max_product(nums: list) -> int:
  inc_subseq = []
  for n in nums:
    if not inc_subseq or n > inc_subseq[-1]:
      inc_subseq.append(n)
    else:
      inc_subseq.append(max(n, inc_subseq[-1] * n))
  return max(inc_subseq)


