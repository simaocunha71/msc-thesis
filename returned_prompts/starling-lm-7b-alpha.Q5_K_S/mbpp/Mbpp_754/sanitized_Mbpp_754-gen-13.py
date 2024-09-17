def extract_index_list(l1: list, l2: list, l3: list) -> list:
  return [i for i in range(len(l1)) if l1[i] in l2 and l1[i] in l3]