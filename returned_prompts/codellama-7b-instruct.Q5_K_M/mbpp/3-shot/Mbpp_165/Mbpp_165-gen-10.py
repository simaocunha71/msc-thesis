
def count_char_position(string_inp: str) -> int:
  char_pos_count = 0
  eng_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  for char in string_inp.lower():
    if char in eng_alphabet:
      if string_inp.lower().index(char) == eng_alphabet.index(char):
        char_pos_count += 1
  return char_pos_count


