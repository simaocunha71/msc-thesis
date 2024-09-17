
def extract_nth_element(tup_list:list,n:int)->list:
  for i in range(len(tup_list)):
    if i == n:
      return tup_list[i][0]
  return "No nth element found"


