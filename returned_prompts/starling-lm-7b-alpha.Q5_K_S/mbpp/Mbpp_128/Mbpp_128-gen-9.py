
def long_words(n,sentence: str) -> list:
  words = sentence.split()
  result = []
  for word in words:
    if len(word) > n:
      result.append(word)
  return result


