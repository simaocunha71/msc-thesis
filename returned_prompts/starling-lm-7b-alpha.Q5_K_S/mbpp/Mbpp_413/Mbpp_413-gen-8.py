"""
def extract_nth_element(tup_list, n):
    return [x[0] for x in tup_list]

def extract_nth_element(tup_list, n):
    return [x for x, _ in tup_list[:n]]
"""

def extract_nth_element(tup_list, n):
    return [tup[0] for tup in tup_list[:n]]


if __name__ == "__main__":
    # assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
    # assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,1)==['Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
    assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,2)==['Wyatt Knott', 'Beau Turnbull']
    assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,3)==['Beau Turnbull']
    assert extract_nth_element([('Greyson Fulton', 9