
def remove_lowercase(string: str) -> str:
  string = list(string)
  for i in range(len(string)):
    if string[i].islower():
      string.pop(i)
  return "".join(string)


