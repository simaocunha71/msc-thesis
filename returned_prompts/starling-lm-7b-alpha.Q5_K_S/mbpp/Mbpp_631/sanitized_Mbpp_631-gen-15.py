def replace_spaces(str):
  res = ""
  for i in range(len(str)):
    if str[i] == "_":
      res += " "
    else:
      res += str[i]
  return res