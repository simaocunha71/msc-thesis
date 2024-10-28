def list_split(my_list,n):
  splitted_list = [my_list[i:i+n] for i in range(0, len(my_list), n)]
  return splitted_list