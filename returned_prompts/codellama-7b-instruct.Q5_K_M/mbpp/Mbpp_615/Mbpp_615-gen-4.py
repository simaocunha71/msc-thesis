
def average_tuple(my_tuple):
  sum = 0
  list = []
  for i in my_tuple:
    sum = sum + sum(i)
    list.append(sum/len(i))
    sum = 0
  return list


