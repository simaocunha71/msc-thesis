
def reverse_vowels(s):
  vowels = "aeiouAEIOU"
  rev_vowels = "".join(reversed([c for c in s if c in vowels]))
  s = s.replace(rev_vowels, rev_vowels[::-1])
  return s


