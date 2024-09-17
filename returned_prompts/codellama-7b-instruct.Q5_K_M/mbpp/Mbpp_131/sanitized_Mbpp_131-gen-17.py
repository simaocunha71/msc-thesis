def reverse_vowels(s):
  vowels = set('aeiou')
  l = list(s)
  left = 0
  right = len(s) - 1
  while left < right:
    while left < len(s) and l[left] not in vowels:
      left += 1
    while right >= 0 and l[right] not in vowels:
      right -= 1
    if left < right:
      l[left], l[right] = l[right], l[left]
    left += 1
    right -= 1
  return ''.join(l)