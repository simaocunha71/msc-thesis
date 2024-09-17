
def pair_xor_Sum(lst: list, n: int) -> int:
  sum = 0
  for i in range(n):
    for j in range(i + 1, n):
        sum += lst[i] ^ lst[j]
  return sum * 2


