def text_match_two_three(text):
  match = re.match(r"a(b{2,3})", text)
  if match:
    return True
  else:
    return False