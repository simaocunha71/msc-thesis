def extract_nth_element(tup_list, n):
    return [i[0] for i in tup_list]

#print(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0))


"""
def extract_nth_element(tup_list, n):
    i = 0
    while i != n:
        if i == n-1:
            return tup_list[i][0]
        else:
            tup_list.pop(0)
            i += 1

#print(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0))
"""

"""
def extract_nth_element(tup_list, n):
    return [tup[0] for tup in tup_list[:n]]

#print(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0))
"""
"""
def extract_nth_element(tup_list, n):
    tup_list.pop(0)
    return [tup[0] for tup in tup_list[:n]]

#print(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0))
"""
"""
def extract_nth