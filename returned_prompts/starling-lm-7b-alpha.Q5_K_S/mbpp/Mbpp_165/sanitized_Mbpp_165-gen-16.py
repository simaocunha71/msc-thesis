def count_char_position(str):
  cnt = 0
  for i in range(len(str)):
    if str[i].lower() == chr(97+i):
      cnt += 1
  return cnt