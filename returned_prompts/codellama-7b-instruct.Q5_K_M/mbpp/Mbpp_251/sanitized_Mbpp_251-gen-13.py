def insert_element(my_list, element):
  new_list = []
  for i in my_list:
    new_list.append(element)
    new_list.append(i)
  return new_list