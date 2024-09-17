def capital_words_spaces(s: str) -> str:
  result = ""
  for i in range(len(s)):
    if i != 0 and s[i].isupper():
      result += " "
    result += s[i]
  return result

