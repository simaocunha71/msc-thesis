
def remove_odd(s: str) -> str:
  odd_characters = []
  for i in range(len(s)):
    if i % 2 == 0:
      odd_characters.append(s[i])
  return "".join(odd_characters)


