
def reverse_string_list(string_list: list) -> list:
  reverse_list = []
  for string in string_list:
    reverse_string = string[::-1]
    reverse_list.append(reverse_string)
  return reverse_list


