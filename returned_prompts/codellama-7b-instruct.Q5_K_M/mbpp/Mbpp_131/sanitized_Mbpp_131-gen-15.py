def reverse_vowels(s):
  vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])
  left = 0
  right = len(s) - 1
  result = ""
  while left < right:
    if s[left] not in vowels:
      result += s[left]
      left += 1
    elif s[right] not in vowels:
      result += s[right]
      right -= 1
    else:
      result += s[right]
      right -= 1
      result += s[left]
      left += 1
  if left == right:
    result += s[left]
  return result