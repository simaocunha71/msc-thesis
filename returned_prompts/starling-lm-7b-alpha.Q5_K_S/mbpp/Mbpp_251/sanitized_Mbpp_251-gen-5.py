def insert_element(list1, element):
  new_list = []
  for i in range(len(list1)):
    new_list.append(element)
    new_list.append(list1[i])
  return new_list