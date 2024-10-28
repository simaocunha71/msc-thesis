def find_adverb_position(sentence: str) -> tuple:
  adverb = ""
  position = 0
  for i in range(len(sentence)):
    if sentence[i].isalpha() and sentence[i].islower():
      adverb += sentence[i]
    else:
      if adverb != "":
        return (position, i, adverb)
      adverb = ""
      position = i+1

