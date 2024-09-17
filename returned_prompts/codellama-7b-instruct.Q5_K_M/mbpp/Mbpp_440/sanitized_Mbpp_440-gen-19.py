def find_adverb_position(sentence: str) -> (int, int, str):
  for i, word in enumerate(sentence.split()):
    if word.endswith('ly'):
      return i, i+1, word
  return -1, -1, ''