def text_match_two_three(text):
  if len(text) < 3:
    return False
  return text[1] == 'b' and text[2] == 'b' and text[0] == 'a'