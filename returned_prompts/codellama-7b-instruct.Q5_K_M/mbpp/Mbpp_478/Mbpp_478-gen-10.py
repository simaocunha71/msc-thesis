
def remove_lowercase(s):
  new_str = ""
  for i in range(len(s)):
    if s[i].isupper():
      new_str += s[i]
  return new_str


