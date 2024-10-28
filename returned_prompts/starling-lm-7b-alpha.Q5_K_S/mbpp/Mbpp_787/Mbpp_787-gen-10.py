
def text_match_three(text):
  if len(text) < 4:
    return False
  if text[0] == "a" and text[1:4] == "bbb":
    return True
  return False


