
def start_withp(words):
  result = []
  for word in words:
    if word.startswith('p'):
      result.append(word)
  return result[:2]


