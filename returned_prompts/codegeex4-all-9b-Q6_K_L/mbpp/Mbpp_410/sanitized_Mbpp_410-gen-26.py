def min_val(heterogeneous_list):
  non_string_list = [i for i in heterogeneous_list if isinstance(i, int)]
  return min(non_string_list)