
def is_Sub_Array(A, B):
  M = len(B)
  N = len(A)
  for i in range(N - M + 1):
    for j in range(M):
      if A[i + j] != B[j]:
        break
    else: 
      return True
  return False

