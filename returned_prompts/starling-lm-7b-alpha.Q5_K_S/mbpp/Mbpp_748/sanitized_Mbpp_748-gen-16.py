def capital_words_spaces(input_string:str)->str:
  return input_string.replace(" " + input_string[0].upper(), input_string[0].upper())