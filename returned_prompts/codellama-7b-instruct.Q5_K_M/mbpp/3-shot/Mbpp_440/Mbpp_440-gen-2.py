
def find_adverb_position(sentence: str) -> tuple:
  adverb_positions = []
  adverbs = ['clearly', 'quickly', 'quick', 'fast', 'well', 'well', 'well', 'well', 'well', 'well', 'well', 'well', 'well']
  for word in sentence.split():
    for index, adv in enumerate(adverbs):
      if word == adv:
        adverb_positions.append((index, len(adverb_positions), word))
  return adverb_positions[0] if adverb_positions else (None, None, None)


