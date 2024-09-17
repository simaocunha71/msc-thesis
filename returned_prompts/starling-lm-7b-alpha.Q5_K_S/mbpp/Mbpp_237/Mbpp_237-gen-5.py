
def check_occurences(input_list: list) -> dict:
  output_dict = {}
  for elem in input_list:
    if elem in output_dict:
      output_dict[elem] += 1
    else:
      output_dict[elem] = 1
  return output_dict


