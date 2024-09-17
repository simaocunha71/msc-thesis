def find_adverb_position(sentence: str) -> tuple:
  words = sentence.split()
  for i, word in enumerate(words):
    if word.endswith('ly'):
      return (i, len(word), word)
  return None