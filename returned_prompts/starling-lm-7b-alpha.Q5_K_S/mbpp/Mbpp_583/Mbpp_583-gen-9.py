
def catalan_number(n: int) -> int:
  catalan = [1, 1]
  for i in range(2,n+1):
    catalan.append(sum(catalan[j] * catalan[i-j-1] for j in range(i)))
  return catalan[n]


