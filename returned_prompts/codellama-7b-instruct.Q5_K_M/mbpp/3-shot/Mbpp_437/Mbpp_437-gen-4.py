
def remove_odd(my_string: str) -> str:
  return ''.join([char for index, char in enumerate(my_string) if index % 2 == 0])


