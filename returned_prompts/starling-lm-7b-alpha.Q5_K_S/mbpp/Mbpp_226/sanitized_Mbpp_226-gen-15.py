def odd_values_string(string):
  even_index_values = [i for i in string if (index + 1) % 2 == 0]
  odd_index_values = [i for i in string if (index + 1) % 2 != 0]
  return "".join(even_index_values) + "".join(odd_index_values)