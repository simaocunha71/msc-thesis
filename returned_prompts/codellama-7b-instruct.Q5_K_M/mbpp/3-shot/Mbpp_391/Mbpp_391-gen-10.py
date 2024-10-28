
def convert_list_dictionary(list_1: list, list_2: list, list_3: list) -> list:
  result = []
  for i in range(len(list_1)):
    temp = {}
    temp[list_1[i]] = {list_2[i]: list_3[i]}
    result.append(temp)
  return result


