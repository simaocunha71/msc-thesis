
def extract_index_list(l1, l2, l3):
  return [i for i in l1 if i in l2 and i in l3 and l1.index(i) == l2.index(i) == l3.index(i)]


