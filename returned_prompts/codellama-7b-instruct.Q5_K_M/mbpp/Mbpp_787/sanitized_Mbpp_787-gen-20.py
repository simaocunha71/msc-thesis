def text_match_three(text):
  pattern = re.compile("a{3}b")
  return bool(pattern.match(text))