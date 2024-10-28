
def text_match_two_three(text):
  return text.count('a') and all(text.count('b') in [2,3] for _ in range(text.count('a')))


