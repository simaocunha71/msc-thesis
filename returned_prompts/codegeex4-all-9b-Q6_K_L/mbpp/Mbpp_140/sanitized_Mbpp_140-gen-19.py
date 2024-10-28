def extract_singly(test_list):
  new_list = []
  for sublist in test_list:
    for element in sublist:
      new_list.append(element)
  return new_list