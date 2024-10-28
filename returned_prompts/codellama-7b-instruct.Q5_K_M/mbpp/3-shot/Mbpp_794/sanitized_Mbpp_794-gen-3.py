import re
def text_starta_endb(text: str) -> bool:
  regex = re.compile(r"a.+b")
  return bool(re.match(regex, text))