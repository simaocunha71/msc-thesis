
def maximize_elements(test_tup1, test_tup2):
  new_tup1 = []
  new_tup2 = []

  for i in test_tup1:
    if i[0] > new_tup1[0][0]:
      new_tup1 = [i]
    elif i[0] == new_tup1[0][0]:
      new_tup1.append(i)

  for i in test_tup2:
    if i[0] > new_tup2[0][0]:
      new_tup2 = [i]
    elif i[0] == new_tup2[0][0]:
      new_tup2.append(i)

  new_tup1_list = []
  for i in new_tup1:
    new_tup1_list.append(i[1])

  new_tup2_list = []
  for i in new_tup2:
    new_tup2_list.append(i[1])

  return (new_tup1, new_tup2_list), (new_tup2, new_tup1_list)


