def insert_element(lst, ele):
    result = []
    for item in lst:
        result += [ele, item]
    return result

print(insert_element(['Red', 'Green', 'Black'], 'c'))

