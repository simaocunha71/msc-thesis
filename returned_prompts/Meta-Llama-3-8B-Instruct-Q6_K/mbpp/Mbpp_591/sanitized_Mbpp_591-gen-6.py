def swap_List(input_list):
  if len(input_list) < 2:
    return input_list
  input_list[0], input_list[-1] = input_list[-1], input_list[0]
  return input_list