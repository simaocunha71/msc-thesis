def remove_lowercase(string):
  new_string = ''
  for i in range(len(string)):
    if not string[i].islower():
      new_string += string[i]
  return new_string