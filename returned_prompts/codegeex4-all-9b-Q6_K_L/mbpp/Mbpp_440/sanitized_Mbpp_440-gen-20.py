import re
def find_adverb_position(sentence):
  pattern = r"\w+ly"
  match = re.search(pattern, sentence)
  if match:
    return (match.start(), match.end(), match.group())
  else:
    return None