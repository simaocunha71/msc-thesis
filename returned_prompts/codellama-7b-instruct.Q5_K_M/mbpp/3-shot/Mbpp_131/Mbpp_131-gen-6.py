
def reverse_vowels(s: str) -> str:
  vowels = 'aeiou'
  rev_vowels = vowels[::-1]
  rev_str = ''
  for c in s:
    if c in rev_vowels:
      rev_str += rev_vowels[vowels.index(c)]
    else:
      rev_str += c
  return rev_str


