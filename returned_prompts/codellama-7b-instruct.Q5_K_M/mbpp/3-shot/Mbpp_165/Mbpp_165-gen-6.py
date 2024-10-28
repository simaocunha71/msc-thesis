
def count_char_position(word):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  count = 0
  for i in range(len(word)):
    if word[i].lower() in alphabet:
      if word[i].lower() == alphabet[i]:
        count += 1
  return count


