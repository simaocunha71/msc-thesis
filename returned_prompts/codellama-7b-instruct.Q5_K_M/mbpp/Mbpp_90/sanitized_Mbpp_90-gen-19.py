def len_log(my_list):
  max_length = 0
  for word in my_list:
    if len(word) > max_length:
      max_length = len(word)
  return max_length