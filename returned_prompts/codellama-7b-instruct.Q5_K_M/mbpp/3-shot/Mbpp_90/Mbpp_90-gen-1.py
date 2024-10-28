
def len_log(my_list: list) -> int:
  longest_word = ""
  for word in my_list:
    if len(word) > len(longest_word):
      longest_word = word

  return len(longest_word)


