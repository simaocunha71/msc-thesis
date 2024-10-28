def convert_list_dictionary(a, b, c):
  zipped_list = zip(a, b, c)
  d = {i: {j: k} for i, j, k in zipped_list}
  return d