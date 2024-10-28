
def convert_list_dictionary(list1,list2,list3):
  result = {}
  for i in range(len(list1)):
    result[list1[i]] = {}
    result[list1[i]][list2[i]] = list3[i]
  return result


