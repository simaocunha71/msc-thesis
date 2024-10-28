
def find_adverb_position(sentence: str) -> tuple:
  for i in range(len(sentence)):
    if sentence[i] in ".,!?":
      return i, sentence[:i].rfind(" "), sentence[:i]
  return len(sentence), -1, ''


