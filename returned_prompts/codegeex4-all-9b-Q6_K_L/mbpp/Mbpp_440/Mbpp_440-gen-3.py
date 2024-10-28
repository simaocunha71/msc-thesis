import re
def find_adverb_position(sentence: str) -> tuple:
  pattern = r'\b\w+\b'
  words = re.findall(pattern, sentence)
  for i, word in enumerate(words):
    if word.endswith('ly'):
      return i, sentence.index(word), word

