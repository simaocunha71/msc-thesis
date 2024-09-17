
def extract_index_list(l1: list,l2: list,l3: list) -> list:
  return [l1[i] for i in range(len(l1)) if l1[i] == l2[i] == l3[i]]


