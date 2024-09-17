def find_Max_Num(digits_list: list) -> int:
  digits_list.sort(reverse = True)
  digits_list = "".join(map(str, digits_list))
  return int(digits_list)