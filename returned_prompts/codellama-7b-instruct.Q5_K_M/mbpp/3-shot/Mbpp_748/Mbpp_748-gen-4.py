
def capital_words_spaces(my_string: str) -> str:
  new_string = ''
  for i in range(len(my_string)):
    if my_string[i].isupper():
      new_string += ' ' + my_string[i]
    else:
      new_string += my_string[i]
  return new_string[1:]


