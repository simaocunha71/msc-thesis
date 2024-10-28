
def occurance_substring(text: str, target: str):
  pos = text.find(target)
  if pos != -1:
    return (target, pos, pos+len(target))
  return None


