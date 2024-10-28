import re
def capital_words_spaces(s: str) -> str:
  return re.sub(r"((?<=[a-z])(?=[A-Z]))", " ", s)