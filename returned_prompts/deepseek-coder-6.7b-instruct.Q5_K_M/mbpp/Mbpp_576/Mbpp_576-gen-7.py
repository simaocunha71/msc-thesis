
def is_Sub_Array(A, B):
  M = len(B)
  N = len(A)
  for i in range(N):
    if (A[i:i+M] == B):
      return True
  return False


