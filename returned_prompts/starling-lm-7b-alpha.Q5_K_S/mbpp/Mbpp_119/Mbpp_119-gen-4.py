
def search(test_list:list):
  for i in range(len(test_list)-1):
    if test_list[i] != test_list[i+1]:
      return test_list[i]
  return test_list[-1]


