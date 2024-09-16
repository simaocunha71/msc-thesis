def extract_index_list(l1, l2, l3):
    return [i for i in set(l1) if l1.count(i) == 3 and i in l2 and i in l3]

# OR
def extract_index_list(l1, l2, l3):
    return [i for i in set(l1) if l1.count(i) == 3 and i in set(l2) and i in set(l3)]

# OR
def extract_index_list(l1, l2, l3):
    return [i for i in set(l1).intersection(l2).intersection(l3) if l1.count(i) == 3]

# OR
def extract_index_list(l1, l2, l3):
    return [i for i in set(l1).intersection(l2).intersection(l3) if l1.count(i) == 3 and l2.count(i) == 3 and l3.count(i) == 3]
