def find_kth(A:list, B:list, k:int) -> int:
  if k > len(A):
    return B[k - len(A) - 1]
  elif k > len(B):
    return A[k - len(B) - 1]
  elif A[k - 1] >= B[k - 1]:
    return A[k - 1]
  else:
    return B[k - 1]