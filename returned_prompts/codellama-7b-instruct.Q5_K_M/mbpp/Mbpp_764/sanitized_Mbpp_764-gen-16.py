def number_ctr(input_string: str) -> int:
  return sum(char.isdigit() for char in input_string)