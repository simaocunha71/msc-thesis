
def occurance_substring(text, substring):
  if substring in text:
    return (substring, text.index(substring), text.index(substring)+len(substring)-1)
  else:
    return None


