
def count_char_position(str: str):
  count = 0
  for i in range(len(str)):
    if ord(str[i]) == ord(chr(i+97)) or ord(str[i]) == ord(chr(i+65)):
      count += 1
  return count


