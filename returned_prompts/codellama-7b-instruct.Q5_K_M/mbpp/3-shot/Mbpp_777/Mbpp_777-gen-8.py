
def find_sum(my_list):
  sum = 0
  for i in my_list:
    if my_list.count(i) == 1:
      sum += i
  return sum


