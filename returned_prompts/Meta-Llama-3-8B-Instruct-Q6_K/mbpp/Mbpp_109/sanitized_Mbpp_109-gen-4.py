def odd_Equivalent(s, times):
  result = 0
  for _ in range(times):
    s = ''.join('1' if c == '0' else '0' for c in s)
  for c in s:
    if c == '1':
      result += 1
  return result