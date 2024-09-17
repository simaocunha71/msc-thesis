def validate(n):
  count = {}
  for digit in str(n):
    if digit in count:
      count[digit] += 1
    else:
      count[digit] = 1
  for digit, freq in count.items():
    if freq > int(digit):
      return False
  return True

