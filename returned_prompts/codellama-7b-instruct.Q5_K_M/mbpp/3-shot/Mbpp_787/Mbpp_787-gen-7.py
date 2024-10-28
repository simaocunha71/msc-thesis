
def text_match_three(text: str) -> bool:
  if re.match(r".*a{3}b.*", text):
    return True
  else:
    return False


