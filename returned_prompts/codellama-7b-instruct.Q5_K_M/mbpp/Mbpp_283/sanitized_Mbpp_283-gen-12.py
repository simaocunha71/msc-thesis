def validate(n):
  digits = [int(i) for i in str(n)]
  for i in range(1,len(digits)+1):
    if digits.count(i) > i:
      return False
  return True