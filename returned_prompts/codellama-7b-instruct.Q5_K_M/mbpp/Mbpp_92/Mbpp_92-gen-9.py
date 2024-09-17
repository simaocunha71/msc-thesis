
def is_undulating(n):
  if n==0:
    return False
  if n[0]==n[-1]:
    return False
  if n[0]==n[1] or n[-1]==n[-2]:
    return False
  if n[0]<n[1] and n[1]>n[2] and n[2]<n[3]:
    return True
  if n[0]>n[1] and n[1]<n[2] and n[2]>n[3]:
    return True
  return False


