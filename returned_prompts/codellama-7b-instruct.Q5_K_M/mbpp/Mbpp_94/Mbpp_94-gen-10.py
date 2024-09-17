
def index_minimum(my_list):
  index = 0
  for i,j in enumerate(my_list):
    if j[1] < my_list[index][1]:
      index = i
  return my_list[index][0]


