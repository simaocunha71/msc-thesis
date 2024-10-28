def reverse_vowels(s):
  vowels = [char for char in s if char.lower() in 'aeiou']
  s = list(s)
  left, right = 0, len(vowels) - 1
  while left < right:
    s[left], s[right] = s[right], s[left]
    left, right = left + 1, right - 1
  return ''.join(s)  # return the modified string