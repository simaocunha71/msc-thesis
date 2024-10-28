
def find_adverb_position(sentence: str) -> tuple:
  adverbs = ['clearly', 'quickly', 'always', 'sometimes', 'never']
  for idx, word in enumerate(sentence.split()):
    if word in adverbs:
      return (idx, word)
  return (-1, None)


