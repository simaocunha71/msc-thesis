def find_kth(a1, a2, k):
  n1, n2 = len(a1), len(a2)
  if k > n1 + n2 or k < 1:
    return None
  if n1 > n2:
    return find_kth(a2, a1, k)
  if n1 == 0:
    return a2[k-1]
  if k == 1:
    return min(a1[0], a2[0])
  i = min(n1, k // 2)
  j = min(n2, k // 2)
  if a1[i-1] > a2[j-1]:
    return find_kth(a1, a2[j:], k-j)
  else:
    return find_kth(a1[i:], a2, k-i)