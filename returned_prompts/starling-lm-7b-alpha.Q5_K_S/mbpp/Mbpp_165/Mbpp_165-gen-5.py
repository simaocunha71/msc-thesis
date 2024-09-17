
def count_char_position(s):
  alpha_dict = {chr(i+97):i for i in range(26)}
  counter = 0
  for i in range(len(s)):
    if s[i].lower() == alpha_dict[s[i]]:
      counter += 1
  return counter


