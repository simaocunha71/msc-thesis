
def count_reverse_pairs(my_list):
  count = 0
  for word in my_list:
    rev_word = word[::-1]
    if rev_word in my_list and word != rev_word:
      count += 1
  return count


