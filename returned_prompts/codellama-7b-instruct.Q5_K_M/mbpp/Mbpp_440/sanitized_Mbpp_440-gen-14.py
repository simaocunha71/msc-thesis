def find_adverb_position(sentence: str) -> tuple:
  for i, word in enumerate(sentence.split()):
    if word[-3:] == 'ly':
      return (i, len(word)-3, word)
  return None