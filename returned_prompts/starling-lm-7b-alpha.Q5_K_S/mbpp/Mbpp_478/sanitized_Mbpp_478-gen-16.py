def remove_lowercase(input_string:str)->str:
  return input_string.replace(str(chr(i) for i in range(97, 97+26)),'')