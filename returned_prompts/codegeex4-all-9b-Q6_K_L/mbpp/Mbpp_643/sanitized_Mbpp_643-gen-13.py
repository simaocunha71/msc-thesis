def text_match_wordz_middle(text: str) -> bool:
  if text[0] == 'z' or text[-1] == 'z':
    return False
  else:
    return 'z' in text[1:-1]