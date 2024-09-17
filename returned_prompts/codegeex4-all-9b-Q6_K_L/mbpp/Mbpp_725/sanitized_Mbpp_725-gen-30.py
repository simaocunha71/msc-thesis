def extract_quotation(s):
  words = s.split(' ')
  result = []
  for word in words:
    if word.startswith('"') and word.endswith('"'):
      result.append(word[1:-1])
  return result