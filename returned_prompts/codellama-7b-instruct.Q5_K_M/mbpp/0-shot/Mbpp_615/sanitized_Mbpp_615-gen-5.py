def average_tuple(my_tuple):
  average_list = []
  for i in my_tuple:
    average = sum(i)/len(i)
    average_list.append(average)
  return average_list