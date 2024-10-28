def convert_list_dictionary(list1:list,list2:list, list3:list) -> list:
  result = []
  for i in range(len(list1)):
    nested_dict = {}
    nested_dict[list1[i]] = {list2[i]: list3[i]}
    result.append(nested_dict)
  return result