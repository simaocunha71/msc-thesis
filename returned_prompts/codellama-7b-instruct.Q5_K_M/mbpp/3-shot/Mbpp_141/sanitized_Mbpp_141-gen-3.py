def pancake_sort(my_list):
  for i in range(len(my_list)-1, 0, -1):
    for j in range(i):
      if my_list[j] > my_list[i]:
        my_list[j], my_list[i] = my_list[i], my_list[j]
    my_list[i:i+1], my_list[0:1] = my_list[0:1], my_list[i:i+1]
  return my_list