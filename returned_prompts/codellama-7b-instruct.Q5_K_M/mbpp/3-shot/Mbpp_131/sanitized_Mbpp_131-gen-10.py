def reverse_vowels(s):
  vowels = set('aeiouAEIOU')
  left = 0
  right = len(s) - 1
  while left < right:
    while left < len(s) and s[left] not in vowels:
      left += 1
    while right >= 0 and s[right] not in vowels:
      right -= 1
    if left < right:
      s[left], s[right] = s[right], s[left]
      left += 1
      right -= 1
  return s