def odd_values_string(string):
  return "".join(string[i] for i in range(len(string)) if i % 2 == 0)