
def remove_Occ(str,char):
  first_occur = str.find(char)
  if first_occur != -1:
    str = str[:first_occur] + str[first_occur+1:]
    last_occur = str.rfind(char)
    if last_occur != -1:
      str = str[:last_occur] + str[last_occur+1:]
  return str


