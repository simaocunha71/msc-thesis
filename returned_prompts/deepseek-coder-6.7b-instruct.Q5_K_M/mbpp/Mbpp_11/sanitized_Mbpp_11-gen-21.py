def remove_Occ(string, char):
  string = string.replace(char, '', 1)
  string = string[::-1]
  string = string.replace(char, '', 1)
  string = string[::-1]
  return string