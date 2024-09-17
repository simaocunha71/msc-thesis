def index_minimum(lst):
  return lst[min(range(len(lst)), key=lambda i: lst[i][1])][0]