def insert_element(lst, ele):
    return [ele] * (len(lst) * 2 - 1) + lst

print(insert_element(['Red', 'Green', 'Black'], 'c'))

