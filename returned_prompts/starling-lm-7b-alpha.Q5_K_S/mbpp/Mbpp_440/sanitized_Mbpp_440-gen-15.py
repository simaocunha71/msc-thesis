def find_adverb_position(sentence:str) -> tuple:
  adverbs = ['quickly', 'suddenly', 'clearly']
  for i, word in enumerate(sentence.split()):
    if word in adverbs:
      return (i, len(word), word)
  return None