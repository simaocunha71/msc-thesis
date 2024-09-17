def count_reverse_pairs(str_list: list) -> int:
  count = 0
  for str1 in str_list:
    for str2 in str_list:
      if str1 == str2[::-1]:
        count += 1
  return count