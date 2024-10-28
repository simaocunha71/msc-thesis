
def count_char_position(s):
  result = 0
  for i in range(len(s)):
    if ord(s[i])-97 == i:
      result += 1
  return result


