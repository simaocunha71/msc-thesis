def toggle_string(s: str) -> str:
  new_str = ""
  for i in range(len(s)):
    new_str+=s[i].upper() if s[i].islower() else s[i].lower()
  return new_str