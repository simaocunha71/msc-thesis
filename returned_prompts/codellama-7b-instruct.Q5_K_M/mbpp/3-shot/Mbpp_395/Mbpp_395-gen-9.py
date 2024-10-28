
def first_non_repeating_character(s: str) -> str:
  for i in range(len(s)):
    if s[i] in s[i+1:]:
      continue
    else:
      return s[i]


