def reverse_words(s: str) -> str:
  words = s.split(" ")
  words = words[::-1]
  return " ".join(words)