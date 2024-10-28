def extract_string(my_list: list, size: int) -> list:
  extracted_list = []
  for i in range(0,len(my_list)):
    if len(my_list[i]) > size:
      extracted_list.append(my_list[i][0:size])
    else:
      extracted_list.append(my_list[i])
  return extracted_list