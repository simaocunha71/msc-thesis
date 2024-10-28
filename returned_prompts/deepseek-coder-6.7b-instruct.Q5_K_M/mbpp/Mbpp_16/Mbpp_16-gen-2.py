
def text_lowercase_underscore(s: str) -> bool:
  return all(x.islower() or x == "_" for x in s.split("_"))


