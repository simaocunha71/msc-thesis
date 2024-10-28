
def find_Max_Num(my_list):
  my_list.sort(reverse=True)
  max_num = ''
  for i in range(len(my_list)):
    max_num += str(my_list[i])
  return int(max_num)


