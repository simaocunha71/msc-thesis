
def number_ctr(string_num: str) -> int:
  return sum(1 for char in string_num if char.isdigit())


