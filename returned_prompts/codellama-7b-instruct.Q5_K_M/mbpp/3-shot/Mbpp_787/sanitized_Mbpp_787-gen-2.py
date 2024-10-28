def text_match_three(text: str) -> bool:
  return re.match(r"a{3}b", text)