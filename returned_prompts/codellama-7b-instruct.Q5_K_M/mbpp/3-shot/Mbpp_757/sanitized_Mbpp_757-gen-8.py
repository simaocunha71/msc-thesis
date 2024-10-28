def count_reverse_pairs(str_list):
  count = 0
  for i in range(len(str_list)):
    for j in range(i+1, len(str_list)):
      if str_list[i][::-1] == str_list[j]:
        count += 1
  return count