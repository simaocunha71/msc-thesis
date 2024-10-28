def remove_odd(string: str) -> str:
  new_string = ""
  for i in string:
    if int(i) % 2 == 0:
      new_string += i
  return new_string