
def text_lowercase_underscore(s):
  for i in range(len(s)):
    if i == 0 and s[i].islower():
      continue
    elif i == len(s) - 1 and s[i].islower():
      continue
    elif s[i] == "_" and s[i + 1].islower():
      continue
    elif s[i].islower() and s[i - 1] == "_":
      continue
    else:
      return False
  return True


