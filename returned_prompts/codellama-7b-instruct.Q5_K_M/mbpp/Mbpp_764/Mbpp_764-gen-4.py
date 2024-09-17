
def number_ctr(str_given):
  count = 0
  for i in str_given:
    if i.isdigit():
      count += 1
  return count


