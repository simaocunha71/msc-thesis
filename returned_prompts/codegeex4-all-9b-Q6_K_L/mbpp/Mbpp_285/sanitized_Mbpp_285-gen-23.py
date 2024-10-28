def text_match_two_three(text: str) -> bool:
  return bool(re.match("ab{2,3}", text))