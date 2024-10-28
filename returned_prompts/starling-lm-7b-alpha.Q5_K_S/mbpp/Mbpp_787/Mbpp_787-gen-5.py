
def text_match_three(text):
  if text.startswith("a") and len(text) > 3:
    return text[1:4] == "bbb"
  else:
    return False


