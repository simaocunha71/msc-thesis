
def is_undulating(n):
  if str(n)[0] == str(n)[-1]:
    return False
  for i in range(1, len(str(n))-1):
    if int(str(n)[i]) > int(str(n)[i-1]) and int(str(n)[i]) > int(str(n)[i+1]):
      continue
    else:
      return False
  return True


