def first_non_repeating_character(s):
  seen_once = {}
  for char in s:
    if char in seen_once:
      seen_once[char] += 1
    else:
      seen_once[char] = 1
  for char, count in seen_once.items():
    if count == 1:
      return char
  return None