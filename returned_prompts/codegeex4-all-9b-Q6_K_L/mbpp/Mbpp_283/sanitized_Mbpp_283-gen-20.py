def validate(n: int) -> bool:
  digit_freq = {}
  for digit in str(n):
    digit_freq[digit] = digit_freq.get(digit, 0) + 1
  for digit, freq in digit_freq.items():
    if freq > int(digit):
      return False
  return True