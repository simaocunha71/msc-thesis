```
def reverse_vowels(string):
  vowels = "aeiouAEIOU"
  reversed_vowels = vowels[::-1]
  return "".join([char if char not in vowels else reversed_vowels[vowels.index(char)] for char in string])
```