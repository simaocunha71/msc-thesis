def add_string(lst, format_string):
  return [format_string.format(i) for i in lst]  # Using list comprehension and string formatting