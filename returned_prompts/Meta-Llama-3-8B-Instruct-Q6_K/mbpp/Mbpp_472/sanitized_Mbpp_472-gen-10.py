def check_Consecutive(lst):
  return all(lst[i] + 1 == lst[i+1] for i in range(len(lst)-1))