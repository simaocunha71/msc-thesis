def sum_list(a_list:list,b_list:list)->list:
  return [a+b for a,b in zip(a_list,b_list)]