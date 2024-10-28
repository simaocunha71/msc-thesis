
def check_occurences(test_list):
  occurences_dict = {}
  for i in test_list:
    if i in occurences_dict:
      occurences_dict[i] += 1
    else:
      occurences_dict[i] = 1
  return occurences_dict


