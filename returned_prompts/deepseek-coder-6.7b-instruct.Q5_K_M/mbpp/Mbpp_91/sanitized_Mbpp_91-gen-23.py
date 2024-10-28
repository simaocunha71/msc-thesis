def find_substring(lst, substr):
  return any(substr in i for i in lst)