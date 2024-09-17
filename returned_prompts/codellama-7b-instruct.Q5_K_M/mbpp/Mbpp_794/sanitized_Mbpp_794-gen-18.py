import re
def text_starta_endb(text: str) -> bool:
  return bool(re.match(r"a.*b", text))