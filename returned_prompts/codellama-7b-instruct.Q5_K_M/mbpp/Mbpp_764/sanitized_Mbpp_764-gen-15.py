def number_ctr(str1:str) -> int:
  return sum(char.isdigit() for char in str1)