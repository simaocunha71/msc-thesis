
def replace_specialchar(sentence):
  special_char = [' ', ',', '.']
  for char in special_char:
    sentence = sentence.replace(char, ':')
  return sentence


