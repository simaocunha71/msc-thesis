def reverse_vowels(s: str) -> str:
  vowels = "aeiou"
  char_list = list(s)
  left = 0
  right = len(s)-1
  while left < right:
    if char_list[left] in vowels:
      while char_list[right] not in vowels:
        right -= 1
      char_list[left], char_list[right] = char_list[right], char_list[left]
      left += 1
    else:
      while char_list[left] not in vowels:
        left += 1
      char_list[left], char_list[right] = char_list[right], char_list[left]
      right -= 1
  return "".join(char_list)