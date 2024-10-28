def count_char_position(string):
  count = 0
  string = string.lower()
  for i in range(len(string)):
    if string[i] == chr(ord('a')+i):
      count += 1
  return count