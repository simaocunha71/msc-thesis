def text_match_wordz_middle(text: str) -> bool:
  if text[0] == 'z' or text[-1] == 'z' or 'z' not in text:
    return False
  else:
    return True