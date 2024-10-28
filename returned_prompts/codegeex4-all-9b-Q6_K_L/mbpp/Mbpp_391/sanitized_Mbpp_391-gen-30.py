def convert_list_dictionary(list1:list,list2:list,list3:list) -> list:
  res = []
  for i in range(len(list1)):
    res.append({list1[i]:{list2[i]:list3[i]}})
  return res