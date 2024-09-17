def convert_list_dictionary(list1: list, list2: list, list3: list) -> list:
  return [{'{}'.format(list1[i]): {list2[i]: list3[i]}} for i in range(len(list1))]