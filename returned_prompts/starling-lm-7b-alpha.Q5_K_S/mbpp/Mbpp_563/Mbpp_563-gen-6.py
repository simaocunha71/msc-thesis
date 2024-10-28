
def extract_values(str):
  new_list = []
  for i in str.split('"'):
    if i != "":
      new_list.append(i)
  return new_list


