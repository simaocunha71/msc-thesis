def remove_Occ(string,char):
  first_index = string.find(char)
  last_index = string.rfind(char)
  return string[:first_index]+string[last_index+1:]