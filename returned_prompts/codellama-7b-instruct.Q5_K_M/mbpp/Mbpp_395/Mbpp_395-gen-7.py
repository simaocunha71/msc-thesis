
def first_non_repeating_character(s: str) -> str:
  count = {}
  for char in s:
    if char not in count:
      count[char] = 1
    else:
      count[char] += 1
  for char in s:
    if count[char] == 1:
      return char


