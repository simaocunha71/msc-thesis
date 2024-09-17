
def toggle_middle_bits(n):
  n = bin(n)[2:]
  if len(n) == 1:
    return 1
  return int(n[:len(n)//2] + ''.join(['0' if s == '1' else '1' for s in n[len(n)//2:]]) + n[len(n)//2:], 2)


