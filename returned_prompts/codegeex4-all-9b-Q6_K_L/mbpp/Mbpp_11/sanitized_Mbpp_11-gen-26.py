def remove_Occ(str: str, char: str):
  str = str.replace(char, '', 1)
  str = str[::-1].replace(char, '', 1)
  return str[::-1]