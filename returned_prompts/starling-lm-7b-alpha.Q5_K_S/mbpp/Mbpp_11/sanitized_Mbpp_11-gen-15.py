def remove_Occ(string, char):
  first_index = string.find(char)
  last_index = string.rfind(char)
  new_str = string[first_index+1:last_index]
  return new_str