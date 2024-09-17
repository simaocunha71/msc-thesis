def extract_index_list(list_1,list_2,list_3):
  common_list = []
  for i in range(len(list_1)):
    if list_1[i] == list_2[i] and list_1[i] == list_3[i]:
      common_list.append(list_1[i])
  return common_list