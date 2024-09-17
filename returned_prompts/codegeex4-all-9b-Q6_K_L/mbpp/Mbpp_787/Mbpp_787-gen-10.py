import re
def text_match_three(string: str):
  match = re.search("ab{3}", string)
  if match:
    return True
  else:
    return False

