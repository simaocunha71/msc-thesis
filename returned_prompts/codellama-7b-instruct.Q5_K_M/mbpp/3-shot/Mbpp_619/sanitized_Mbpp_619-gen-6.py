def move_num(str_input):
  num_list = [int(i) for i in str_input if i.isdigit()]
  num_str = ''.join([str(i) for i in num_list])
  non_num_str = ''.join([i for i in str_input if not i.isdigit()])
  return non_num_str + num_str